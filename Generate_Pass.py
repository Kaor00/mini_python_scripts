import random
from string import digits, punctuation, ascii_letters


symbols = digits + punctuation + ascii_letters
# n = input('Укажите длинну пароля: ')
sec_random = random.SystemRandom()
# password = ''.join(sec_random.choice(symbols) for i in range(int(n)))
password = ''.join(sec_random.choice(symbols) for i in range(15))
print(f'Ваш пароль: {password}')

# закоментированные строки для создания пароля выборочной длинны