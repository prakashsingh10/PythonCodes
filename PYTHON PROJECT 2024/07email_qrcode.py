import qrcode
email_address = "prakashsinghthakuri1030@gmail.com"
subject ="job appointmeant"
body = "prakash you are selected for the post of vice pressident"
email =f"mailto:{email_address}?subject={subject}&body={body}"
img = qrcode.make(email)
type(img)
img.save("email.png")#wifi qr code maker