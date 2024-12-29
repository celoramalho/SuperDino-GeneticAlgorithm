import numpy as np
import cv2 as cv
from classes.image_processing import ImageProcessing

class Screenshot(ImageProcessing):
    def __init__(self, image):
        self.image = image
        #print(f"Image type in init Screenshot: {type(self.image)}")
        super().__init__(image)
        #self.pixels_ocurrences = None
        #self.eightbit_array = None
        #self.background_color = None
    
    def process_img(self):
        img_processed = self.process()
        #print(f"Image type in process_img Screenshot: {type(img_processed)}")
        return Screenshot(img_processed)
        
    def show(self):
        #print(f"Image type in show Screenshot: {type(self.image)}")
        resized_image = cv.resize(self.image, (0, 0), fx=0.5, fy=0.5)
        cv.imshow("Computer Vision", resized_image)
    
    """
    def detect_contours(self):
        contours, hierarchy = cv.detectContours(self.screenshot_array, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        return contours, hierarchy
    
    def detect_elements(self):
        contours, hierarchy = self.detect_contours()
        elements = {"dino": None, "cactus": None, "fcking_prehistoric_birds": None}
        all_elements = []
    
        cactus = []
        dinos = []
        fcking_prehistoric_birds = []

        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(self.screenshot_array, (x, y), (x + w, y + h), (255, 0, 0), 2)

            aspect_ratio = w / float(h)
            if self.detect_dino(aspect_ratio, h, w):
                dinos.append([x, y, w, h])
            elif self.detect_cactus(aspect_ratio, h, w):
                cactus.append([x, y, w, h])
            elif self.detect_fcking_prehistoric_birds(aspect_ratio, h, w):
                fcking_prehistoric_birds.append([x, y, w, h])

        elements["dino"] = dinos
        elements["cactus"] = cactus
        elements["fcking_prehistoric_birds"] = fcking_prehistoric_birds
        return elements
    
    def detect_dino(self, aspect_ratio, h, w): #bidimensional (2D)        
        if 20 < w < 60 and 20 < h < 60 and 0.5 < aspect_ratio < 1.5:
            return True
        else:
            return False
    
    def detect_cactus(self, aspect_ratio, h, w): #bidimensional (2D)
        if 20 < w < 60 and 20 < h < 60 and 0.5 < aspect_ratio < 1.5:
            return True
        else:
            return False
    
    def detect_fcking_prehistoric_birds(self, aspect_ratio, h, w): #bidimensional (2D)
        if 20 < w < 60 and 20 < h < 60 and 0.5 < aspect_ratio < 1.5:
            return True
        else:
            return False

        #maped_pixels = []        

        #for row in self.screenshot_array:
        #   for pixel in row:
        #        if pixel in mapped_pixels.values():
        #            maped_pixels[pixel]["occurrences"] += 1
        #        else:
        #            maped_pixels.append({"pixel": pixel, "gray_value": color, "occurrences": 1})

"""
    #def print_pixels_ocurrences(self):
    #    print("Gray levels occurrences:")
    #    for gray, count in self.pixels_ocurrences.items():
    #        if count > 10:
    #            print(f"Gray value {gray}: {count} ocurrences")

    #def detect_common_color(screenshot_array):

    #def detect_pixels_ocurrences(self):
    #    unique_values, counts = np.unique(self.screenshot_array, return_counts=True)
    #    pixels_ocurrences = dict(zip(unique_values, counts))
    #    sorted_pixels_ocurrences = dict(
    #        sorted(pixels_ocurrences.items(), key=lambda x: x[1], reverse=True) #Timsort
    #    )
    #    self.pixels_ocurrences = sorted_pixels_ocurrences
    
    #def detect_common_color(self):
    #    self.detect_pixels_ocurrences()
    #    most_common_color = next(iter(self.pixels_ocurrences.keys()))
    #    return most_common_color