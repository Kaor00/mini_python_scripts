from PIL import Image

img = Image.open('/home/kaor/Изображения/месяц безлимита 1900.png')
blackAndWhite = img.convert('L')
blackAndWhite.save('bw.png')
