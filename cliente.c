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


void entrada_diario(int network_socket)
{
    char message[256];
    printf("Insira uma mensagem para o diário de hoje\n");
    fgets(message, sizeof(message), stdin);
    message[strcspn(message, "\r\n")] = 0;
    char diario_msg[300];
    snprintf(diario_msg, sizeof(diario_msg), "/diario %s", message);
    if (send(network_socket, diario_msg, strlen(diario_msg) + 1, 0) == -1)
    {
        printf("Erro ao enviar mensagem do diário\n");
    }
}

void iniciar_cliente(int network_socket)
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
            server_response[bytes] = '\0';
            server_response[strcspn(server_response, "\r\n")] = 0;
            if (strncmp(server_response, "/diario ", 8) == 0) // strncmp compara um número definido de caracteres nas strings
            {
                printf("\n[Diário] %s\n", server_response + 8);
            }

            else
            {
                printf("\n[Servidor] %s\n> ", server_response); // resposta originária de outro cliente
            }
            fflush(stdout);
        }
    }

    else
    {
        printf("Para enviar uma mensagem ao diário, use /diario (mensagem), para usar o chat, apenas digite normalmente, para voltar ao menu, digite sair\n");
        char message[256];
        while (1)
        {

            printf("> ");
            fflush(stdin);
            fgets(message, sizeof(message), stdin);
            message[strcspn(message, "\n")] = 0;

            if (strcmp(message, "sair") == 0)
            {
                printf("Encerrando conexão...\n");
                break;
            }
            if (strncmp(message, "/diario ", 8) == 0)
            {
                entrada_diario(network_socket);
                continue;
            }
            if (send(network_socket, message, strlen(message) + 1, 0) == -1)
            {
                printf("Erro ao enviar mensagem\n");
                break;
            }
        }
        close(network_socket);
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

    return 0;
}