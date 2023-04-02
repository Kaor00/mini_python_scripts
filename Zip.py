from zipfile import ZipFile

# Для примера имени файла
file_name = '/полный путь.zip'

with ZipFile(file_name, 'r') as zip_file:
    print('Zip all files...')

    zip_file.printdir()
    zip_file.extractall()

    print('Zip done successful!')
# Файл распаковывается в папку этого скрипта.
