import os


restart = input("Do you want to restart your PC? (yes/no): ")

if restart == 'no':
    exit()
else:
    os.system("shutdown /r /t 5")
# /s - Завершение работы компьютера
# /r - Завершение работы и перезагрузка компьютера
# /t - Задание задержки в ххх секунд перед завершением работы компьютера
