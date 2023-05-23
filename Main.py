import cv2

def withCamera():
    cap = cv2.VideoCapture(0)  # 0, default camera

    while True:
        ret, frame = cap.read()  # Capture a frame from the camera

        # Convert the frame to grayscale to find the QR codes
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use QR code detection function to find QR codes
        qr_code_detector = cv2.QRCodeDetector()
        decoded_text, _, _ = qr_code_detector.detectAndDecode(gray)

        # If QR codes are found, draw bounding boxes and display the decoded text
        if decoded_text is not None:
            cv2.putText(frame, decoded_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            print("QR Code URL:", decoded_text)
            break
        # Display the frame
        cv2.imshow('QR Reader', frame)

        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

def withImage():
    # Specify the file path of the image you want to read the QR code from
    image_path = input("Enter the image file path: ")

    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use QR code detection function to find QR codes
    qr_code_detector = cv2.QRCodeDetector()
    decoded_text, _, _ = qr_code_detector.detectAndDecode(gray)

    # If QR codes are found, display the decoded text
    if decoded_text is not None:
        cv2.putText(image, decoded_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        print("QR Code URL:", decoded_text)


    # Display the image
    cv2.imshow('QR Reader', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

question = input("Which function do you want to use? (withCamera or withImage): ")

while True:
    if question == "withCamera":
        withCamera()
    elif question == "withImage":
        withImage()
    else:
        print("Wrong input!")

    question = input("Which function do you want to use? (withCamera or withImage): ")
