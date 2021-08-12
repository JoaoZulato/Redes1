import socket

HOST = 'localhost'
PORT = 36000

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen()
print('Aguardando conexao')
conn, ender = s.accept()

print('Conectado em ',ender)

while True:
    data = conn.recv(1024)
    if not data:
        print('fechando a conexao')
        conn.close()
        break
    conn.sendall(data)