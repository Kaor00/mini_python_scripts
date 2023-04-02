import pyshorteners


url = 'https://animego.online/360-chernyj-klever-v142-b1.html'

print(f'Ссылка после сокращения: {pyshorteners.Shortener().tinyurl.short(url)}')
