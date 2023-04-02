import qrcode

url = ''

img = qrcode.make(url)
img.save("AAA.png")

print("[+] QR code done")
