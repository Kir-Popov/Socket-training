import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 12343))

server.listen(4)
print('Start')

while True:
    client_socket, address = server.accept()
    data = client_socket.recv(1024).decode('utf-8')
    print(data)
    my_list = ['0', '1']

    genetate_num = random.choice(my_list)

    client_socket.send(genetate_num.encode("utf-8"))
