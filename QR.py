#Code to read the QR image

import cv2

# Ask user for image file path
image_path = input("Enter the path to the QR code image: ")

# Read the image & checks if loaded correctly
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image. Please check the path.")
else:
    # Initialize QRCode detector
    detector = cv2.QRCodeDetector()

    # Detect and decode the QR code
    # data --> extracted information
    # bbox --> Boundary or coordinate of four corner of the QR
    # _ --> Straightened version of the QR 
    data, bbox, _ = detector.detectAndDecode(image)

    if data:
        print(f"QR Code data:\n{data}")
    else:
        print("No QR Code found in the image.")
