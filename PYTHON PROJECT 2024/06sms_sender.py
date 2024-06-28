#wifi qr code maker
import qrcode

phone_number ="9868936598"
message= "hello how are you messi"
sms =f"SMSTO:<phone_number>:<message>"
img = qrcode.make(sms)
type(img)
img.save("sms.png")#wifi qr code maker

