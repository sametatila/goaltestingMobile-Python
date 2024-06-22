import qrcode

def generate_qr_code(text, width, height):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((width, height))
    img.save("qr_code.png")

# Example usage
text = "proctor/26-03-2024/Bilfen Cayyolu Ilkokulu/1/4-A"
width = 300
height = 300
generate_qr_code(text, width, height)