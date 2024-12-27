import numpy as np
import cv2 as cv
from .convolution_kernel import ConvolutionKernel

class Screenshot(ConvolutionKernel):
    def __init__(self, screenshot_array, kernel):
        self.screenshot_array = screenshot_array
        self.pixels_ocurrences = None
        self.background_color = None
        self.convolution_kernel = ConvolutionKernel(kernel)
        self.eightbit_array = None
        self.dino_coords = None

    def process(self):
        self.background_color = self.find_common_color()
        self.screenshot_array = self.convolution_kernel.apply_convolution(self.screenshot_array)
        self.dino_coords = self.identify_dino()              

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
        

    def identify_dino(self): #bidimensional (2D)
        
        contours, _ = cv.findContours(self.screenshot_array, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)   
        
        dino_contour = None
        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)
            aspect_ratio = w / float(h)

            # Filter based on size and aspect ratio (adjust values for your game)
            if 20 < w < 60 and 20 < h < 60 and 0.5 < aspect_ratio < 1.5:
                dino_contour = (x, y, w, h)
                break

        dino_coords = dino_contour # identify_dino()
        if dino_coords:
            x, y, w, h = dino_coords 
            
            print(f"Dino found at: x={x}, y={y}, width={w}, height={h}")
            
            self.screenshot_array = cv.cvtColor(self.screenshot_array, cv.COLOR_GRAY2BGR)
            # Draw a rectangle around the Dino
            cv.rectangle(self.screenshot_array, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        else:
            print("Dino not found!")
            

        #maped_pixels = []        

        #for row in self.screenshot_array:
        #   for pixel in row:
        #        if pixel in mapped_pixels.values():
        #            maped_pixels[pixel]["occurrences"] += 1
        #        else:
        #            maped_pixels.append({"pixel": pixel, "gray_value": color, "occurrences": 1})
