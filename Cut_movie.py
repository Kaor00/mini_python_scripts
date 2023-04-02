from moviepy.editor import *


clip = VideoFileClip('')

clip = clip.subclip(0, 30)

# clip.ipython_display(width=360)
# Команда проигрывания через питона не работает

clip.write_videofile('')
