import socket

HOST = 'localhost'  # endereço IP ou nome do servidor
PORT = 5000  # porta usada pel3o servidor

# cria o socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta ao servidor
c.connect((HOST, PORT))

term = False
print('Digite sair para terminar o Chat')

while not term:
    c.send(input('Mensagem:').encode('utf-8'))
    msg = c.recv(1024).decode('utf-8')
    if msg == 'sair':
        term = True
    else:
        print(msg)

c.close()