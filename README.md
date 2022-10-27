# piSecurityCamera2
Improved pi Security Camera using OpenCV

It uses a template method design pattern to try different approaches for detection and notification

Also replaces the original PiCamera with OpenCV camera module for image capture, which seems to have some issues using the standard raspberryPi camera (I got sequential photos with quite different image luminosity and color). This affects my detection algorithm accuracy.

# Dependencies
- [OpenCV](https://pysource.com/2018/10/31/raspberry-pi-3-and-opencv-3-installation-tutorial/)
- Pillow