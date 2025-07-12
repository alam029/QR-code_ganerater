#Code to read the QR image
import cv2
# For creting QR Code
import qrcode
# To creating Images and Show
from PIL import Image

# read data from qr code
def read_qr(image_path):
    # Read the image & checks if loaded correctly
    image = cv2.imread(image_path)
    # Initialize QRCode detector
    detector = cv2.QRCodeDetector()
    # Detect and decode the QR code
    # data --> extracted information
    # bbox --> Boundary or coordinate of four corner of the QR
    # _ --> Straightened version of the QR 
    data, bbox, _ = detector.detectAndDecode(image)
    return data

# create QR Code
def create_qr(data):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=3, #Increase for comlexity upto 40
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # L, M, Q, H (for recovery if scratched, blur, etc)
        box_size=10,
        border=4,
    )
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# main
print("""
-----Create & Read QR code-----
1) Create QR Code.
2) Fetch data from QR Code.
""")
try:
    user_inp = int(input("Enter your choise (1 & 2 ): "))
    if(user_inp == 1):
        # Data to encode
        data = input("Enter Important Data: ")
        img = create_qr(data)
        # Save the image
        img.save("my_qr_code.png")
        print("QR code generated and saved as my_qr_code.png")
        # show QR code
        show_img = input("Do you want seen QR Code (y/n): ")
        if(show_img.lower() == "y"):
            image = Image.open("my_qr_code.png")
            image.show()

    elif(user_inp == 2):
        # Ask user for image file path
        image_path = input("Enter the path to the QR code image: ")
        data = read_qr(image_path)
        if data:
            print(f"QR Code data:\n{data}")
        else:
            print("No QR Code found in the image.")
    else:
        print("Enter only 1 or 2.")
except ValueError:
    print("Enter only numbers!!!!")