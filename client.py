import socket
import threading
import time


PORT = 5050
FORMATO = 'utf-8'
SERVER = #IP DO SERVER
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

    

def handle_mensagens():
    while (True):
        msg = client.recv(1024)
        if (msg):
            print("RETORNO= ",msg.decode('utf-8'))

def enviar_para_server(mensagem):
    client.send(mensagem.encode(FORMATO))

def enviar_mensagem():
    while True:
        mensagem = input("Send command: ")
        enviar_para_server(mensagem)




def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2  = threading.Thread(target=enviar_mensagem)
    thread1.start()
    thread2.start()


iniciar()