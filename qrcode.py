import segno
# asking user to create value for Qr code to be Generted
while True:
    url = str(input("enter the url : "))
    if url <= 0:
        print("enter vaild url to generate Qr code ")
        break
    qrcode = segno.make_qr({url})
    qrcode.save(f"{url}.png")
    print("QR code has been generated successfully!")