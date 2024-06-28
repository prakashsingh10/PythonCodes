
import qrcode
img = qrcode.make('Prakash singh thakuri')
type(img)  # qrcode.image.pil.PilImage
img.save("prakashman.png")