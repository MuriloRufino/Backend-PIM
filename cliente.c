#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <signal.h>
#define PORT 8080
static PyObject *pModule = NULL;
void python_inicializar(const char *nomearquivo)
{
    FILE *fp = fopen(nomearquivo, "r");
    if (!fp)
    {
        perror("Erro ao abrir arquivo Python");
        return;
    }
    Py_Initialize();
    PyRun_SimpleString("import sys; sys.path.append('.')");

    PyRun_SimpleFile(fp, nomearquivo);
    Py_Finalize();
    fclose(fp);
}
int main()
{

    // criação do socket
    int network_socket = socket(AF_INET, SOCK_STREAM, 0);
    // especificando endereço
    struct sockaddr_in server_address;

    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = inet_addr("127.0.0.1"); // no oficial, vai ser outro IP

    int connection = connect(network_socket, (struct sockaddr *)&server_address, sizeof(server_address));

    if (connection == -1)
    {
        printf("Erro na conexão\n");
    }
    else
    {
        char credencial[15], senha[20];
        printf("Insira sua credencial e sua senha\n");
        fgets(credencial, sizeof(credencial), stdin);
        credencial[strcspn(credencial, "\n")] = 0;
        fgets(senha, sizeof(senha), stdin);
        senha[strcspn(senha, "\n")] = 0;
        send(network_socket, credencial, sizeof(credencial), 0);
        send(network_socket, senha, sizeof(senha), 0);
        fflush(stdin);
        char response[256];
        memset(response, 0, sizeof(response));
        int bytes = recv(network_socket, response, sizeof(response), 0);
        if (bytes <= 0)
        {
            printf("Servidor desconectado ou erro na recepção.\n");
        }

        if (strcmp(response, "Login Válido") == 0)
        {
            int continuar = 1;
            while (continuar)
            {
                
                python_inicializar("app.py");

                pid_t pid = fork();

                if (pid == 0)
                {
                    char server_response[256];
                    while (1)
                    {
                        memset(server_response, 0, sizeof(server_response));
                        int bytes = recv(network_socket, server_response, sizeof(server_response), 0);
                        if (bytes <= 0)
                        {
                            printf("Servidor desconectado ou erro na recepção.\n");
                            break;
                        }
                        // resposta originária de outro cliente
                        printf("\n[Servidor] %s\n> ", server_response);
                        fflush(stdout);
                    }
                }

                else
                {
                    char message[256];
                    while (1)
                    {
                        printf("digite uma mensagem: > ");
                        fflush(stdin);
                        fgets(message, sizeof(message), stdin);
                        message[strcspn(message, "\n")] = 0;

                        if (strcmp(message, "sair") == 0)
                        {
                            printf("Encerrando conexão...\n");
                            break;
                        }

                        if (send(network_socket, message, strlen(message), 0) == -1)
                        {
                            printf("Erro ao enviar mensagem\n");
                            break;
                        }
                    }
                }
                char opcao;
                printf("Deseja voltar ao menu?[S/n]\n");
                scanf("%c", &opcao);
                if (opcao == 'S' || opcao == 's')
                {
                    continuar = 1;
                }
                else
                {
                    continuar = 0;
                    close(network_socket);
                    kill(pid, SIGKILL);
                }
                int c;
                while ((c = getchar()) != '\n' && c != EOF);
            }
        }
        else
        {
            printf("%s\n", response);
        }

        return 0;
    }
}