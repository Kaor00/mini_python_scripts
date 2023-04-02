from PIL import Image, ImageFilter

# Узнать параметры
img = Image.open("плакатный.png")

print(f"IMG format: {img.format}\nIMG size: {img.size}")

# Сменить формат
img.save("плакатный.jpg", "png")

img2 = Image.open("плакатный.jpg")

# Сделать размытие
saved = "New_img.jpg"
blurred = img2.filter(ImageFilter.BLUR)
blurred.save(saved)
img2.show()
blurred.show()

# Изменить размер
img3 = Image.open("New_img.jpg")

size = (128, 128)
saveds = "New_img_small.jpg"

img3.thumbnail(size)
img3.save(saveds)
img3.show()

# Команда Show() открывает файл для просмотра.
