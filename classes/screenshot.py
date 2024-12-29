import numpy as np
import cv2 as cv
from classes.image_processing import ImageProcessing

class Screenshot(ImageProcessing):
    def __init__(self, image):
        self.image = image
        super().__init__(image)
    
    def process_img(self):
        img_processed = self.process()
        return Screenshot(img_processed)
        
    def show(self):
        resized_image = cv.resize(self.image, (0, 0), fx=0.5, fy=0.5)
        cv.imshow("Computer Vision", resized_image)