from captcha.image import ImageCaptcha


image = ImageCaptcha(width=250, height=120)
text = "Pil56req"

data = image.generate(text)

image.write(text, "captcha.png")

# Не работает
