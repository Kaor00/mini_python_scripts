import pafy

url = 'https://www.youtube.com/watch?v=cPl0fnUTSrg'

try:
    video = pafy.new(url)
    streams = video.streams
    best_stream = video.getbest()
    best_stream.download()
    print('Video successful upload!')
except Exception:
    print('Oops. Something wrong...')
# не работает плагин.
