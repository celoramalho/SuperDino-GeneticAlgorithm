import numpy as np
import cv2 as cv
from classes.image_processing import ImageProcessing

class Screenshot(ImageProcessing):
    
    screen_show_mode = "Objects_Detecteds"
    
    @classmethod
    def define_show_mode(cls, mode="Objects_Detecteds"):
        modes_available = ["Computer_Vision", "Original", "Objects_Detecteds"]
        if mode in modes_available:
            cls.screen_show_mode = mode
        else:
            raise ValueError(f"Invalid show mode: {mode}. Available modes: {modes_available}")
    
    def __init__(self, image):
        self.image = image
        super().__init__(image)
    
    def process_img(self):
        image_processed = self.process(Screenshot.screen_show_mode)
        return Screenshot(image_processed)
        
    def show(self):
        resized_image = cv.resize(self.image, (0, 0), fx=0.5, fy=0.5)
        cv.imshow(Screenshot.screen_show_mode, resized_image)