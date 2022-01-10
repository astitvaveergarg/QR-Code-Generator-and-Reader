import cv2
Text = input("Enter The QR Code:")
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread(Text))
print("Decoded text is: ", val)