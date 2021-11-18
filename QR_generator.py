import qrcode

data = input("enter the data to create QR >> ")

qr = qrcode.make(data)

qr.save("C:/Users/Nithin/onedrive/desktop/qrnew0.png")

print("succesfully saved to your desktop")