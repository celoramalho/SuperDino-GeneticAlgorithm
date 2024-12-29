import numpy as np
import cv2 as cv
from classes.image_processing import ImageProcessing

class Screenshot(ImageProcessing):
    def __init__(self, image, objects_detecteds_img=None, computer_vision_img=None):
        self.image = image
        self.objects_detecteds_img = objects_detecteds_img
        self.computer_vision_img = computer_vision_img
        super().__init__(image)
    
    def process_img(self):
        img_processed, objects_detecteds_img, computer_vision_img = self.process()
        return Screenshot(img_processed, objects_detecteds_img, computer_vision_img)
        
    def show(self, mode="Original"):
        
        match mode:
            case "Computer_Vision":
                img_to_show = self.computer_vision_img
            case "Original":
                img_to_show = self.image
            case "Objects_Detecteds":
                img_to_show = self.objects_detecteds_img
            case _:
                img_to_show = self.objects_detecteds_img
            
        resized_image = cv.resize(img_to_show, (0, 0), fx=0.5, fy=0.5)
        cv.imshow("Computer Vision", resized_image)