import QRcode
text=input("enter what you want convert: ")
QR=QRcode.make(text)
QR.save('qrcode_result.jpg')