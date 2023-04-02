import os
import shutil


source = 'AAA.txt'
destination = 'trash'

os.mkdir(destination)

path = shutil.move(source, destination)
print(path)

new_name = 'AAA.txt'
final_path = shutil.move(path, new_name)
print(final_path)

# Для удобной манипуляции с файлами и папками в стандартной библиотеки
# Python существует специальный модуль shutil.
# Функция shutil.move(source, destination) позволяет вам переместить
# любой файл или папку (даже непустую). Обратите внимание, что если
# destination — это уже существующая папка, то файл/папка будет
# перемещена внутрь неё, в остальных случаях файл/папка будут
# скопированы точно по нужному адресу.
# В случае успеха, функция вернёт новое местоположение файла.
# Если destination существует и не является папкой, то будет выброшена ошибка.
