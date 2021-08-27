import socket
import threading


#HOST = input("Host: ")
#PORT = int(input("Port: "))

HOST ='localhost'
PORT = 1997

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST,PORT))
server.listen()
print("*********Bem vindo ao JOMA chat**********")
print(f'Servidor ligado e escutando \nendereço: {HOST}\nporta: {PORT}')
clients = []
usernames = []
        
            
            
def lista_online():
    
        
	for client in clients:
	    online = online + client + '\n'
     
	return online[:-1]

def globalMessage(mensagem):
 
  
    for client in clients:
        client.send(mensagem)
    
    return mensagem

def handleMessages(client):
    while True:
        try:
            receiveMessageFromClient = client.recv(2048).decode('utf-8')
            
            globalMessage(f'{usernames[clients.index(client)]}: {receiveMessageFromClient}'.encode('ascii'))
        except:
            clientLeaved = clients.index(client)
            client.close()
            clients.remove(clients[clientLeaved])
            clientLeavedUsername = usernames[clientLeaved]
            print(f'{clientLeavedUsername} Saiu do chat :(')
            globalMessage(f'{clientLeavedUsername} Se foi'.encode('utf-8'))
            usernames.remove(clientLeavedUsername)



def initialConnection():
    while True:
        try:
            client, address = server.accept()
            print(f"Nova conexão: {str(address)}")
            clients.append(client)
            client.send('Usuario'.encode('utf-8'))
            username = client.recv(2048).decode('utf-8')
            usernames.append(username)
            globalMessage(f'{username} entrou no chat'.encode('utf-8'))
            
            user_thread = threading.Thread(target=handleMessages,args=(client,))
            user_thread.start()
        except:
            pass

initialConnection()

