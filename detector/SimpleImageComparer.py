from common.DetectionLevel import DetectionLevel
from PIL import Image, ImageChops
from PIL import ImageFilter
import statistics
import math
import cv2

'''
    Simple image comparator based on movement detection
'''
class SimpleImageComparer:

    '''
        Constructor: define detection tresholds and store the original image
    '''
    def __init__(self, img):
        self.minThreshold = 10
        self.maxThreshold = 100
        self.original = self._process_image(img)


    '''
        Pre-process the image
        - Convert image to RGB color space
        - Transform to PIL image (TODO - work with cv2 image only)
        - Apply gaussian blur and then reduce to 8x8 image (why? gaussian blur merges neighbor pixels and resize reduces the search space)
    '''
    def _process_image(self, image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(img)
        im_pil.filter(ImageFilter.GaussianBlur(2)).resize((8, 8), Image.LANCZOS)
        return im_pil

    '''
        Calculate the diff from 2 images by returning an absolute value
        It calculates the pixel diff from Image A and Image B and then the AVG pixel value
    '''
    def _diff_images(self, a, b):
        diff = ImageChops.difference(self._process_image(a), self._process_image(b))
        diff_list = list(diff.getdata())

        # Converting a list of tuples to list
        difference = statistics.mean(map(math.fsum, diff_list))

        print("Image diff value: {}".format(difference))

        return difference

    '''
        calculate the image diff and then return the detection leven
    '''
    def compare_images(self, a, b):
        diff = self._diff_images(a, b)

        if diff >= self.maxThreshold:
            return DetectionLevel.HIGH
        if diff >= self.minThreshold:
            return DetectionLevel.LOW
        return DetectionLevel.NONE
