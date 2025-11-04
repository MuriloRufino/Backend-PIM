#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 8080
// Funções para abrir o arquivo inicio.py e validar o login
void python_inicializar(const char *nomearquivo);
void python_finalizar();
int python_login(const char *credencial, const char *senha);
void python_cadastro(const char *credencial, const char *senha);

static PyObject *pModule = NULL;
static PyObject *pFuncLogin = NULL;
static PyObject *pFuncCadastro = NULL;

void python_inicializar(const char *nomearquivo)
{
    Py_Initialize();
    PyRun_SimpleString("import sys; sys.path.append('.')");
    PyObject *pName = PyUnicode_DecodeFSDefault(nomearquivo);
    pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule)
    {
        pFuncLogin = PyObject_GetAttrString(pModule, "login");
        pFuncCadastro = PyObject_GetAttrString(pModule, "cadastro");
    }
    else
    {
        PyErr_Print();
        fprintf(stderr, "Erro ao importar %s.py\n", nomearquivo);
    }
}
void python_finalizar()
{
    Py_XDECREF(pFuncLogin);
    Py_XDECREF(pFuncCadastro);
    Py_XDECREF(pModule);
    Py_Finalize();
}

int python_login(const char *credencial, const char *senha)
{
    if (!pFuncLogin)
        return 0;
    PyObject *pArgs = PyTuple_Pack(2, PyUnicode_FromString(credencial), PyUnicode_FromString(senha));
    PyObject *pValue = PyObject_CallObject(pFuncLogin, pArgs);
    int result = PyObject_IsTrue(pValue);
    Py_XDECREF(pArgs);
    Py_XDECREF(pValue);
    return result;
}
void python_cadastro(const char *credencial, const char *senha)
{
    if (!pFuncCadastro)
        return;
    PyObject *pArgs = PyTuple_Pack(2, PyUnicode_FromString(credencial), PyUnicode_FromString(senha));
    PyObject *pValue = PyObject_CallObject(pFuncCadastro, pArgs);
    Py_XDECREF(pArgs);
    Py_XDECREF(pValue);
}

void passar_mensagens(int from, int to) //fonte: IA
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

        send(to, buffer, bytes, 0);
    }

    close(from);
    close(to);
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
    server_address.sin_addr.s_addr = INADDR_ANY; //no oficial, vai ser INADDR_ANY
    struct sockaddr_in client_address;
    socklen_t addrsize = sizeof(client_address);
    // ligando o socket no ip e porta especificados, setsockopt usado para garantir que a porta esteja desocupada
    int opt = 1;
    setsockopt(server_socket, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
    bind(server_socket, (struct sockaddr *)&server_address, sizeof(server_address));
    //"escutando" conexões
    listen(server_socket, 2);
    printf("Escutando\n");

    pid_t childpid;
    int client_sockets[2], cnt = 0, client_socket, num_clients = 0;
    while (1)
    {

        client_socket = accept(
            server_socket, (struct sockaddr *)&client_address,
            &addrsize);
    
        if (client_socket < 0)
        {
            printf("Erro no clientsocket\n");
            exit(1);
        }

        printf("Clientes conectados: %d\n\n",
               ++cnt);

        char credencial[15], senha[20];
        int bytes = recv(client_socket, credencial, sizeof(credencial), 0);
        int bytes1 = recv(client_socket, senha, sizeof(senha), 0);
        if (bytes <= 0)
        {
            printf("Servidor não recebeu a credencial\n");
        }
        if (bytes1 <= 0)
        {
            printf("Servidor não recebeu a senha\n");
        }
        python_inicializar("inicio");
        char *message;
        if (python_login(credencial, senha))
        {
            message = "Login Válido";
        }
        else{
            message = "Login inválido, tenha certeza de digitar os dados corretamente ou, caso não tenha o feito, faça seu cadastro";
        }
        send(client_socket, message, strlen(message) + 1, 0);

        python_finalizar();
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

    return 0;
}