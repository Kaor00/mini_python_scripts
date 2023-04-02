from PIL import Image

img = Image.open('')
blackAndWhite = img.convert('L')
blackAndWhite.save('bw.png')
