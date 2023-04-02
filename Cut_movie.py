from moviepy.editor import *


clip = VideoFileClip('/home/kaor/PycharmProjects/Qwark/Download_by_PY/Examples/AAA.mp4')

clip = clip.subclip(0, 30)

# clip.ipython_display(width=360)
# Команда проигрывания через питона не работает

clip.write_videofile('/home/kaor/PycharmProjects/Qwark/Download_by_PY/Examples/clip.mp4')
