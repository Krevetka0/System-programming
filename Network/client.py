import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print("Подключено к {} порт {}".format(*server_address))
sock.connect(server_address)

try:
    mess = input()
    print(f'Отправка: {mess}')
    message = mess.encode()
    sock.sendall(message)

    amount_recieved = 0
    amount_expected = len(message)
    while amount_recieved < amount_expected:
        data = sock.recv(100)
        amount_recieved += len(data)
        mess = data.decode()
        print(f'Получено: {data.decode()}')
finally:
    print('Закрываем сокет')
    sock.close()
