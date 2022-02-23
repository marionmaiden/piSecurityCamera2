from abc import abstractmethod, ABC

from common.DetectionLevel import DetectionLevel

'''
    Template method for the motion detector
'''


class DetectorTemplate(ABC):

    @abstractmethod
    def capture(self):
        pass

    @abstractmethod
    def notify(self, img, level):
        pass

    @abstractmethod
    def detect_change(self, img1, img2):
        pass

    """
        Simple motion detector mechanism
        - We take a base photo
        - Loop
            - We take another photo (current) and compare both
                - If they are different, we notify and the current photo becomes the base photo
    """

    def run_detector(self):

        original_image = self.capture()

        while 1:

            current_image = self.capture()

            level = self.detect_change(original_image, current_image)

            if level > DetectionLevel.NONE:
                self.notify(current_image, level)
                original_image = current_image
