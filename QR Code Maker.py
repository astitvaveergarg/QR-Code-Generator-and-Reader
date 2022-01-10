import qrcode
Text = input("Enter The Text Here: ")
QR= qrcode.make(Text)
QR.save("QRCODE.jpg")
