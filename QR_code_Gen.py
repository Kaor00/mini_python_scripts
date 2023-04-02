import qrcode

url = 'https://t.me/Ka_acustic'

img = qrcode.make(url)
img.save("AAA.png")

print("[+] QR code done")
