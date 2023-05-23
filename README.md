# QR Code Reader 📷

This code allows you to read QR codes using the camera or from an image file. It utilizes the OpenCV library for image processing and QR code detection.

## Prerequisites

Make sure you have the following dependencies installed:

- OpenCV (cv2)

## Usage

1. Clone or download the code files to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the code files.

### Reading QR codes with the camera

1. Run the code using the following command:

```bash
python Main.py
```

2. The program will prompt you to choose the function to use: `withCamera` or `withImage`. Enter `withCamera` to use the camera for real-time QR code detection.

3. The program will open a window showing the camera feed. Hold a QR code in front of the camera.

4. If a QR code is detected, a bounding box will be drawn around it, and the decoded text will be displayed on the image window and printed to the console.

5. Press the 'q' key to exit the program.

### Reading QR codes from an image file

1. Run the code using the following command:

```bash
python Main.py
```

2. The program will prompt you to choose the function to use: `withCamera` or `withImage`. Enter `withImage` to read QR codes from an image file.

3. Enter the file path of the image file you want to read the QR code from when prompted.

4. If a QR code is detected in the image, the decoded text will be displayed on the image window and printed to the console.

5. Close the image window to exit the program.

## Example

Here's an example usage of the code:

```bash
Which function do you want to use? (withCamera or withImage): withCamera
```

The code will open the camera feed, and when a QR code is detected, it will display the decoded text and print it to the console. To exit, press the 'q' key.

```bash
Which function do you want to use? (withCamera or withImage): withImage
Enter the image file path: path/to/image.jpg
```

The code will load the specified image and if a QR code is detected, it will display the decoded text on the image window and print it to the console. Close the image window to exit the program.

