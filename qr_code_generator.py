import qrcode
import os

# Set the URL for your GitHub page
url = os.getenv('QR_DATA_URL', 'https://github.com/ErcihanK')  # Replace with your GitHub URL if needed

# Set the output file path
output_dir = os.getenv('QR_CODE_DIR', '.')
filename = os.getenv('QR_CODE_FILENAME', 'github_qr.png')

# Generate and save the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(os.path.join(output_dir, filename))

print("QR code generated and saved as", filename)
