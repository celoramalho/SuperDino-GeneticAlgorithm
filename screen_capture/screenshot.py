import numpy as np
import cv2 as cv
from .convolution_kernel import ConvolutionKernel

class Screenshot(ConvolutionKernel):
    def __init__(self, screenshot_array):
        self.screenshot_array = screenshot_array
        self.pixels_ocurrences = None
        self.background_color = None

    def process(self):
        self.background_color = self.find_common_color()
        pass

    #def find_common_color(screenshot_array):

    def find_pixels_ocurrences(self):
        unique_values, counts = np.unique(self.screenshot_array, return_counts=True)
        pixels_ocurrences = dict(zip(unique_values, counts))
        sorted_pixels_ocurrences = dict(
            sorted(pixels_ocurrences.items(), key=lambda x: x[1], reverse=True) #Timsort
        )
        self.pixels_ocurrences = sorted_pixels_ocurrences
    
    def find_common_color(self):
        self.find_pixels_ocurrences()
        most_common_color = next(iter(self.pixels_ocurrences.keys()))
        return most_common_color

    def print_pixels_ocurrences(self):
        print("Gray levels occurrences:")
        for gray, count in self.pixels_ocurrences.items():
            if count > 10:
                print(f"Gray value {gray}: {count} ocurrences")

    def show_screenshot(self):
        cv.imshow("Computer Vision", self.screenshot_array)
        

    def locate_dino_game(self): #bidimensional (2D)
        
        pixels_ocurrences = self.find_pixels_ocurrences(self.screenshot_array)
        background_color = np.equal(self.screenshot_array, [0, 0, 0])

        #maped_pixels = []        

        #for row in self.screenshot_array:
        #   for pixel in row:
        #        if pixel in mapped_pixels.values():
        #            maped_pixels[pixel]["occurrences"] += 1
        #        else:
        #            maped_pixels.append({"pixel": pixel, "gray_value": color, "occurrences": 1})
