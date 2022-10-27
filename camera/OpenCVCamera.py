import cv2

'''
    Implements the Camera and image capture function
'''


class OpenCVCamera:

    def __init__(self):
        self.camera = cv2.VideoCapture(0)

    def __del__(self):
        self.camera.release()

    '''
        Capture a image using OpenCV camera module
    '''
    def capture(self):
        _, frame = self.camera.read()
        return frame
