from threading import Thread


def file(thefile, num):
    with open(thefile, 'w', encoding="UTF-8") as f:
        for i in range(num):
            if num > 500:
                f.write('Больше 500\n')
            else:
                f.write('Меньше 500\n')


thread1 = Thread(target=file, args=('f1.txt', 200,))
thread2 = Thread(target=file, args=('f2.txt', 1000,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
