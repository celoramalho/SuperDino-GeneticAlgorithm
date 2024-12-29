import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

class ImageProcessing():
        
    kernels = {
        "Laplacian": np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]),
        "Sobel X": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
        "Sobel Y": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
        "Emboss": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]),
        "Kirsch Compass": np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]]),
        "Prewitt X": np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]),
        "Prewitt Y": np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]),
    }

    def __init__(self, image):
        self.cv_image = image
        self.kernel = self.kernels['Laplacian']

    def process(self):
        blurred_img = self.blur_image(self.cv_image)
        gray_img = self.convert_to_gray(blurred_img)
        sharp_img = self.apply_convolution(gray_img)
        resized_img = self.resize_image(sharp_img)
        binary_img = self.threshold_image(resized_img)
        
        elements = self.detect_elements(binary_img)

        objects_detecteds_image = self.draw_detected_objects(self.cv_image, elements)
        original_image = self.resize_image(self.cv_image)
        return original_image, objects_detecteds_image, binary_img
    
    def draw_detected_objects(self, img, elements):
        img = self.draw_and_log_elements(img, elements["dino"], "Dino", (0, 255, 0))  # Green
        img = self.draw_and_log_elements(img, elements["cactus"], "Cactus", (0, 0, 255))  # Red
        img = self.draw_and_log_elements(img, elements["fcking_prehistoric_birds"], "Fcking Prehistoric Birds", (0, 0, 192))
        return img# Dark Red
    
    def draw_and_log_elements(self, img, elements, label, color):
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 0.3
        thickness = 1
        
        if elements:
            for element in elements:
                x, y, w, h = element
                cv.putText(img, label, (x, y - 10), font, font_scale, color, thickness)
                print(f"{label} found at: x={x}, y={y}, width={w}, height={h}")
                cv.rectangle(img, (x, y), (x+w, y+h), color, 2)
        
    def apply_convolution(self, cv_image):
        filtered_image = cv.filter2D(cv_image, -1, self.kernel)
        return filtered_image
    
    def eightbit_image(self, cv_image):
        eightbit_array = np.uint8(np.absolute(cv_image))
        return eightbit_array
    
    def blur_image(self, cv_image):
        return cv.GaussianBlur(cv_image, (3, 3), 0)
    
    def resize_image(self, cv_image):
        return cv.resize(cv_image, None, fx=0.60, fy=0.60)
    
    def threshold_image(self, cv_image):
        binary =  cv.adaptiveThreshold(cv_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2) #Convert to Binary
        return binary
    
    def convert_to_gray(self, cv_image):
        return cv.cvtColor(cv_image, cv.COLOR_BGR2GRAY)
    
    def convert_to_bgr(self, cv_image):
        return cv.cvtColor(cv_image, cv.COLOR_GRAY2BGR)
    
    def find_contours(self, cv_image):
        contours, hierarchy = cv.findContours(cv_image, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
        return contours, hierarchy
    
    def detect_elements(self, image):
        contours, hierarchy = self.find_contours(image)
        elements = {"dino": None, "cactus": None, "fcking_prehistoric_birds": None,"unknown": None}

        cactus = []
        dinos = []
        fcking_prehistoric_birds = []
        unknown = []
        #print(f"Shape in detect_elements method: {cv_image.shape}")
        
        
        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)

            aspect_ratio = w / float(h)
            if self.detect_dino(aspect_ratio, h, w):
                is_new = True
                for existing_dino in dinos:
                    if self.is_duplicate(existing_dino, contour):
                        is_new = False
                        break
                if is_new:
                    dinos.append([x, y, w, h])
                    #cv.drawContours(self.computer_img, contour, 0, (0, 255, 0), 4)
                    
            elif self.detect_cactus(aspect_ratio, h, w):
                cactus.append([x, y, w, h])
                #cv.drawContours(self.computer_img, contour, 0, (255, 0, 0), 4)
            elif self.detect_fcking_prehistoric_birds(aspect_ratio, h, w):
                fcking_prehistoric_birds.append([x, y, w, h])
                #cv.drawContours(self.computer_img, contour, 0, (255, 0, 0), 4)
            else:
                unknown.append([x, y, w, h])
                #cv.drawContours(self.computer_img, contour, 0, (255, 255, 0), 4)

        elements["dino"] = dinos
        elements["cactus"] = cactus
        elements["fcking_prehistoric_birds"] = fcking_prehistoric_birds
        elements["unknown"] = unknown
        return elements
    
    def is_duplicate(self, existing_object, new_object, threshold=10):
        ex, ey, ew, eh = existing_object
        x, y, w, h = cv.boundingRect(new_object)
        if abs(x - ex) < threshold and abs(y - ey) < threshold:
            return True
        else:
            return False
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