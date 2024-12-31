import cv2 as cv
import numpy as np

class ObjectDetected:
    
    min_area = 300
    min_perimeter = 50
    
    def __init__(self, contour, label, reference_images):
        self.contour = contour
        self.x, self.y, self.w, self.h = cv.boundingRect(contour)
        self.label = label
        self.area = self.w * self.h
        self.aspect_ratio = self.w / float(self.h)
        self.reference_contours = reference_images
        self.aprox = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
        
        
    def dimensions(self):
        return (self.x, self.y, self.w, self.h)
    
    def height(self):
        return self.h   
    def lenght(self):
        return self.w
    
    def width(self):
        return self.h
    
    def location(self):
        return (self.x, self.y)
    
    def is_dino(self): #bidimensional (2D)
        dino_standup_contour = self.reference_contours["dino_up"]
        dino_aprox = cv.approxPolyDP(dino_standup_contour, 0.01 * cv.arcLength(dino_standup_contour, True), True)
        similarity = cv.matchShapes(dino_standup_contour, self.contour, cv.CONTOURS_MATCH_I1, 0)
        
        if self.area >= self.min_area:
            if similarity < 0.15:
                print(f"similarity: {similarity}, position: {self.x}, {self.y}")
                self.label = "dino"
                return True
            else:
                return False
        
    def is_cactus(self): #bidimensional (2D)
        if 20 < self.w < 60 and 20 < self.h < 60 and 0.5 < self.aspect_ratio < 1.5:
            self.label = "cactus"
            return False
        else:
            return False
    
    def is_fcking_prehistoric_birds(self): #bidimensional (2D)
        if 20 < self.w < 60 and 20 < self.h < 60 and 0.5 < self.aspect_ratio < 1.5:
            self.label = "fcking_prehistoric_birds"
            return False
        else:
            return False
    def get_contour_reference_objects(self, image):
        img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        #blurred_image = cv.GaussianBlur(img_gray, (3, 3), 0)
        image_resized = cv.resize(img_gray, None, fx=0.60, fy=0.60)
        kernel_sharpening = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        img_sharpened = cv.filter2D(image_resized, -1, kernel_sharpening)
        eightbit = np.uint8(np.absolute(img_sharpened))#8-bit vallues within range 0 to 255

        _, binary = cv.threshold(eightbit, 30, 255, cv.THRESH_BINARY)
        
        contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)     
        object_contour = contours[0]
        
        return object_contour
    
