from PIL import Image
from pyzbar.pyzbar import decode


decoded = decode(Image.open('AAA.png'))
print(decoded[0].data)
