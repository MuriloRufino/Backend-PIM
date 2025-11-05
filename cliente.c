#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <signal.h>
#define PORT 8080
// gcc cliente.c -o cliente -I/usr/include/python3.12 -lpython3.12
void iniciar_cliente(int network_socket)
{

    int continuar = 1;
    while (continuar)
    {

        pid_t pid = fork();

        if (pid == 0)
        {
            while (1)
            {
                char server_response[256];
                memset(server_response, 0, sizeof(server_response));

                int bytes = recv(network_socket, server_response, sizeof(server_response), 0);
                if (bytes <= 0)
                {
                    printf("Servidor desconectado ou erro na recepção.\n");
                    break;
                }
                // resposta originária de outro cliente
                server_response[bytes] = '\0';
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
                    continuar = 0;
                    break;
                }

                if (send(network_socket, message, strlen(message) + 1, 0) == -1)
                {
                    printf("Erro ao enviar mensagem\n");
                    break;
                }
            }
        }
    }
}
void entrada_diario(int network_socket)
{
    char message[256];
    printf("Insira uma mensagem para o diário de hoje\n");
    scanf(" %s", message);
    if (send(network_socket, message, strlen(message) + 1, 0) == -1)
    {
        printf("Erro ao enviar mensagem\n");
    }
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
    iniciar_cliente(network_socket);
    char op;
    printf("Deseja inserir uma mensagem no diário eletrônico?[S/n]\n");
    scanf("%c", &op);
    if (op == 'S'){
        entrada_diario(network_socket);
    }
    
    return 0;
}