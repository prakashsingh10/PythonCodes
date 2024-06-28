#wifi qr code maker
import qrcode
img = qrcode.make("wifi")

wifi_type ="WPA"
wifi_ssid ="iampms_fpkhr"
wifi_password = "prakash1234@"
wifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)
img.save("wifi.png")