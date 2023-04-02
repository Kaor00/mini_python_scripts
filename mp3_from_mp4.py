import moviepy.editor as me


video = me.VideoFileClip("/полный путь AAA.mp4")
video.audio.write_audiofile("AAA.mp3")
