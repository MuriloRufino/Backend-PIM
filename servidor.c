#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#define PORT 8080

void passar_mensagens(int from, int to) // fonte: IA
{

    char buffer[256];
    while (1)
    {
        memset(buffer, 0, sizeof(buffer));
        int bytes = recv(from, buffer, sizeof(buffer), 0);
        if (bytes <= 0)
        {
            break;
        }
        buffer[strcspn(buffer, "\r\n")] = 0;
        if (strncmp(buffer, "/diario", 7) == 0)
        {
            send(to, buffer, strlen(buffer) + 1, 0);
            send(from, buffer, strlen(buffer) + 1, 0);
            continue;
        }
        
        send(to, buffer, bytes, 0);
        
    }

    close(from);
    close(to);
}

void trocar_mensagens(int server_socket, int client_socket, struct sockaddr_in client_address, socklen_t addrsize)
{

    int cnt = 0, num_clients = 0, client_sockets[2];
    while (1)
    {

        client_socket = accept(
            server_socket, (struct sockaddr *)&client_address,
            &addrsize);

        if (client_socket < 0)
        {
            printf("Erro no socket do cliente\n");
            exit(1);
        }

        printf("Clientes conectados: %d\n\n",
               ++cnt);

        client_sockets[num_clients++] = client_socket;

        if (num_clients == 2)
        {

            if (fork() == 0)
            {
                close(server_socket);
                passar_mensagens(client_sockets[0], client_sockets[1]);
                exit(0);
            }

            if (fork() == 0)
            {
                close(server_socket);
                passar_mensagens(client_sockets[1], client_sockets[0]);
                exit(0);
            }

            num_clients = 0; // reseta o contador para aceitar uma nova dupla
        }
    }
}

int main()
{

    // criando socket do servidor
    int server_socket;
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    // definindo endereço
    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(PORT);
    server_address.sin_addr.s_addr = inet_addr("127.0.0.1"); // no oficial, vai ser INADDR_ANY
    struct sockaddr_in client_address;
    socklen_t addrsize = sizeof(client_address);
    // ligando o socket no ip e porta especificados, setsockopt usado para garantir que a porta esteja desocupada
    int opt = 1;
    setsockopt(server_socket, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    bind(server_socket, (struct sockaddr *)&server_address, sizeof(server_address));
    //"escutando" conexões
    listen(server_socket, 2);
    printf("Escutando\n");
    int client_sockets[2], client_socket;
    trocar_mensagens(server_socket, client_socket, client_address, addrsize);
    
    return 0;
}