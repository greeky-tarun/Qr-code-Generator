import qrcode

# Create a QR code from the URL
myqr = qrcode.make("https://greeky-tarun.github.io/Portfolio/")

# Save the QR code as a PNG file
myqr.save("myqr.png")
