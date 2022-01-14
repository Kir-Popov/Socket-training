import time
from multiprocessing import Process, Queue
from flask import Flask
from flask import render_template
from flask import request

from tcp_client import send_string_to_pic


def flask_server(my_list: Queue):
    app = Flask(__name__)

    @app.route("/", methods=['GET'])
    def get_vvod():
        return render_template('vvod.html')

    @app.route("/", methods=['POST'])
    def post_vvod():
        string = request.form['text']
        my_list.put(string)
        print(my_list)
        print(id(my_list))
        return render_template('vvod.html')

    app.run()


def tcp_process(my_queue: Queue):
    while True:
        print('Пытаемся отправить сообщение')
        send_string_to_pic(my_queue)
        time.sleep(5)


def main():
    my_queue = Queue()
    p1 = Process(target=flask_server, args=(my_queue,))
    p2 = Process(target=tcp_process, args=(my_queue,))
    p2.start()
    p1.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    main()

