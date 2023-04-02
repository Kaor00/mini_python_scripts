import threading

print('Поиск ошибок')


def check_errors():
    print('Не удалось найти ошибки в работе программы.')


timer = threading.Timer(5.0, check_errors)
timer.start()
