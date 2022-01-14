import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12343))

server.listen(4)
print('Start')

while True:
    client_socket, _ = server.accept()
    _ = client_socket.recv(1024).decode('utf-8')
    my_list = ['0', '1']
    genetate_num = random.choice(my_list)
    client_socket.send(genetate_num.encode("utf-8"))

    if genetate_num == '1':
        client_socket, _ = server.accept()
        data = client_socket.recv(1024).decode('utf-8')
        # И вот эту штуку мы уже выводим на табло
        print(data)
