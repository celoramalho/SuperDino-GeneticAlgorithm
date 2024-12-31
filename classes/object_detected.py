import cv2 as cv
import numpy as np
import os

class ObjectDetected:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
    reference_contours = {}
    reference_images = {
        "dino_up": os.path.join(PARENT_DIR, "img", "dino_up.png"),
        "cactus": os.path.join(PARENT_DIR, "img", "cactus-1.png"),
        "fcking_prehistoric_birds": os.path.join(PARENT_DIR, "img", "prehistoric_bird.png")
    }

    min_area = 300
    min_perimeter = 50

    @classmethod
    def get_contour_reference_objects(cls, image):
        img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        blurred_image = cv.medianBlur(img_gray, 1)
        kernel_sharpening = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        img_sharpened = cv.filter2D(blurred_image, -1, kernel_sharpening)
        eightbit = np.uint8(np.absolute(img_sharpened))#8-bit vallues within range 0 to 255

        _, binary = cv.threshold(eightbit, 30, 255, cv.THRESH_BINARY)
        
        contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)    
        if contours:
            object_contour = contours[0]
            return object_contour
        else:
            raise ValueError("No contour found in the image.")

    @classmethod
    def initialize_reference_contours(cls):
        print("Initializing reference contours...")
        """Carrega e processa as imagens de referência, armazenando seus contornos."""
        for name, path in cls.reference_images.items():
            print(f"Loading reference image: {path}")
            cv_image = cv.imread(path)
            if cv_image is not None:
                cls.reference_contours[name] = cls.get_contour_reference_objects(cv_image)
            else:
                raise FileNotFoundError(f"Error: Image {path} not found or could not be loaded.")

    
    def __init__(self, contour, label):
        self.contour = contour
        self.x, self.y, self.w, self.h = cv.boundingRect(contour)
        self.label = label
        self.area = self.w * self.h
        self.aspect_ratio = self.w / float(self.h)
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
        dino_standup_contour = ObjectDetected.reference_contours["dino_up"]
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
    
    def show_reference_contours():
        images = {}
        for name, path in ObjectDetected.reference_images.items():
            images[name] = cv.imread(path)
        
            cv.imshow(name, images[name])
            cv.waitKey(0)
            cv.destroyAllWindows()
             
        list(images.keys())
                    
        for name, contour in ObjectDetected.reference_contours.items():
            print(f"Nome: {name}")
            canvas = np.zeros_like(images[name])
            cv.drawContours(canvas, [contour], -1, (255, 255, 255), thickness=2)

            cv.imshow(name, canvas)
            cv.waitKey(0)
            cv.destroyAllWindows()
