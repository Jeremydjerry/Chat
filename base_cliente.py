"""
Lado do Cliente: usa socket para mandar data para o servidor e imprime a resposta do servidor para cada linha na mensagem. Podemos colocar o host como sendo 'localhost' para indicar que o servidor está na mesma máquina. Para rodar através da internet é preciso colocar o servidor em outra máquina e passar para o nome do host o endereço de IP ou nome do domínio.

"""

from socket import *

# Configurações de conexão do servidor
# o nome do servidor pode ser o endereço de IP ou domínio (ola.python.net)
serverHost = 'localhost'
serverPort = 17311

# Mensagem a ser mandada codificada em bytes


# Criamos o socket e o conectamos ao servidor
sockobj = socket (AF_INET, SOCK_STREAM)
sockobj.connect ((serverHost, serverPort))

# Mandamos a mensagem linha por linha
while True:
    mensagem = input ("Você: ")
    sockobj.send (bytes(mensagem, "utf8"))
    if mensagem == "sair":
        sockobj.send(bytes("O cliente saiu do ar", "utf8"))
        sockobj.close ()
    
    # Depois de mandarmos uma linha esperamos a resposta do servidor
    data = sockobj.recv (1024)
    print ("Ele: ", data.decode ())

# Fechamos a conexão
sockobj.close ()
