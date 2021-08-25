import socket
import threading

print("*********Bem vindo ao JOMA chat**********")
ServerIP = input("Endereço do servidor:: ")
PORT = int(input("Porta: "))

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try: 
    username = input('Nome de usuario: ')
    client.connect((ServerIP,PORT))
    print(f'Conectado a {ServerIP}:{PORT}')
except:
    print(f' {ServerIP}:{PORT} Algum dos elementos nao esta certo')

def Mensagem():
    teste=True
    while teste==True:
        try:
            message = client.recv(2048).decode('ascii')
            if message=='getUser':
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print('Erro, servidor offline ou dados incorretos')
            teste=False

def mandaMensagem():
    while True:
        client.send(input().encode('ascii'))

thread1 = threading.Thread(target=Mensagem,args=()) 
thread2 = threading.Thread(target=mandaMensagem,args=())

thread1.start()
thread2.start()