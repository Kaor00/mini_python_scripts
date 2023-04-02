import pytesseract
from PIL import Image


img = Image.open("AAA.jpg")

file_name = img
file_name = file_name.split()[0]

text = pytesseract.image_to_string(img).strip()
print(text)

with open(f"{file_name}.txt", "w") as text_file:
    text_file.write(text)

# Не работает...
