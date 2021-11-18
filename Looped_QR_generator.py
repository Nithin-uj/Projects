import qrcode
qrnew1 = 1

print('''Note:-
This program Cotains Loop,
When you Everytime Create a QR Will Saved To Desktop and Thea Old QR Will be Deleted''')

while(True):
     data = input("enter the data to create QR >> ")

     qr = qrcode.make(data)

     qr.save("C:/Users/Nithin/onedrive/desktop/newqr.png")

     if qrnew1==1:
         print("You Have Created ", qrnew1,"st QR_code")

     elif qrnew1==2:
         print("You Have Created ", qrnew1,"nd QR_code And The Old QR was deleted")

     elif qrnew1==3:
         print("You Have Created ", qrnew1,"rd QR_code And The Old QR was deleted")

     else:
         print("You Have Created ", qrnew1,"th QR_code And The Old QR was deleted")
     qrnew1+=1
     print("succesfully saved to your desktop")