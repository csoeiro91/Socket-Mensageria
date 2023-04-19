import socket

HOST = 'localhost'  # endereço IP do servidor, vazio significa todos os IPs disponíveis
PORT = 5000  # porta para escutar as conexões

# cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# liga o socket ao endereço e porta especificados
s.bind((HOST, PORT))

# espera por conexões
s.listen(1)

# aceita uma conexão
conn, addr = s.accept()

term = False

while not term:
    msg = conn.recv(1024).decode('utf-8')
    if msg == 'sair':
        term = True
    else:
        print(msg)
        conn.send(input('Mensagem: ').encode('utf-8'))

conn.close()
s.close()

