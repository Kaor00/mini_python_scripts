import pyqrcode


QRString = 'https://t.me/Ka_acustic'
url = pyqrcode.create(QRString)
url.png('AAA.png', scale=8)
