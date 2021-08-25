import socket
import threading

#HOST = input("Host: ")
#PORT = int(input("Port: "))

HOST ='localhost'
PORT = 1997

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print("*********Bem vindo ao JOMA chat**********")
print(f'Servidor ligado e escutando \nendereço: {HOST}\nporta: {PORT}')
clients = []
usernames = []

def globalMessage(message,compara):
    for client in clients:
        client.send(message)

def handleMessages(client):
    while True:
        try:
            receiveMessageFromClient = client.recv(2048).decode('ascii')            
            globalMessage(f'{usernames[clients.index(client)]}: {receiveMessageFromClient}'.encode('ascii'))
            
        except:
            clientLeaved = clients.index(client)
            client.close()
            clients.remove(clients[clientLeaved])
            clientLeavedUsername = usernames[clientLeaved]
            print(f'{clientLeavedUsername} Saiu do chat :(')
            globalMessage(f'{clientLeavedUsername} Se foi'.encode('ascii'))
            usernames.remove(clientLeavedUsername)



def initialConnection():
    while True:
        try:
            client, address = server.accept()
            print(f"Nova conexão: {str(address)}")
            clients.append(client)
            client.send('getUser'.encode('ascii'))
            username = client.recv(2048).decode('ascii')
            usernames.append(username)
            globalMessage(f'{username} entrou no chat'.encode('ascii'))
            user_thread = threading.Thread(target=handleMessages,args=(client,))
            user_thread.start()
        except:
            pass

initialConnection()

