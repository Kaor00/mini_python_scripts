import pyqrcode


QRString = ''
url = pyqrcode.create(QRString)
url.png('AAA.png', scale=8)
