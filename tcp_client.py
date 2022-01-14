import socket
from multiprocessing import Queue


def send_string_to_pic(my_queue: Queue):

    if my_queue.empty():
        print('Очередь пуста')
        return

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 12343))
    client.send(bytes('1', encoding='utf8'))
    data = client.recv(1024).decode('utf-8')
    client.close()

    if data == '1':
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 12343))
        string_to_send = my_queue.get_nowait()
        print('Отправляем на пик', string_to_send)
        client.send(bytes(string_to_send, encoding='utf8'))
        client.close()
    else:
        print('Получили 0, ждем 5 сек')
