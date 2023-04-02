import moviepy.editor as me


video = me.VideoFileClip("/Download_by_PY/Examples/AAA.mp4")
video.audio.write_audiofile("AAA.mp3")
