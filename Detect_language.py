from langdetect import detect

while True:
    data = input('Enter word or phrase: ')
    print(detect(data))
