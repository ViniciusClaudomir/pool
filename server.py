import socket
import threading
import time
from poolThread import Pool
from functions import FUNC
from random import randint

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER_IP, PORT)
FORMATO = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

conexoes = []
mensagens = []

WORKERS = 5
pool = Pool(WORKERS)
pool.initialize_pool()

def send_callback(msg):
    callback = msg.__annotations__
    message_to_bytes = str.encode(callback['msg'] +"  "+ str(msg.result()))
    callback['conn'].send(message_to_bytes)

def handle_client(conn, addr):
    print(f"New conection receive, IP: {addr}")
    global conexoes, pool
    nome = False
    while (True):
        msg = conn.recv(1024).decode(FORMATO)
        if (msg):
            print(msg)
            command = msg.split("#")[0]
            args = [x.strip() for _, x in enumerate(msg.split('#')) if _ > 0]
            print(args)
            func = FUNC[command]

            annotations_from_callback = {
                'conn':conn,
                'client': addr,
                'msg': f"Processo de {command} para {args[0]} e {args[1]} finalizado"}
            command_sorted = command + "_" + str(randint(1,500))

            pool.execute_function(command_sorted,annotations_from_callback, 'call_1', func, args[0], args[1])

def start():

    server.listen()
    print(f"Socker server initialize in port {PORT}")
    while 1:
        conn, addr = server.accept()
        thread =  threading.Thread(target=handle_client, args = (conn, addr))
        thread.start()


pool.callback = {'call_1':send_callback}
start()