from template.DetectorTemplate import DetectorTemplate
from camera.OpenCVCamera import OpenCVCamera
from detector.SimpleDetector import SimpleDetector
from notifier.SimpleEmailNotifier import SimpleEmailNotifier
from common.DetectionLevel import DetectionLevel
import datetime


class SimpleMotionDetector(DetectorTemplate):

    def __init__(self):
        self.camera = OpenCVCamera()
        self.detector = SimpleDetector(self.camera.capture())
        self.notifier = SimpleEmailNotifier()

    def capture(self):
        return self.camera.capture()

    def notify(self, img, level):
        if level == DetectionLevel.LOW:
            print("low level detection at %s" % datetime.datetime.now())
        elif level == DetectionLevel.HIGH:
            print("high level detection at %s" % datetime.datetime.now())

    def detect_change(self, img1, img2):
        return self.detector.compare_images(img1, img2)
