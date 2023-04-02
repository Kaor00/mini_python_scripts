import pyshorteners


url = 'https://....html'

print(f'Ссылка после сокращения: {pyshorteners.Shortener().tinyurl.short(url)}')
