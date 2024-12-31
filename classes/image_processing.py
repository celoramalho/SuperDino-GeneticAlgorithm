import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from classes.object_detected import ObjectDetected

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

    def process(self, screen_show_mode = "Objects_Detecteds"):
        computer_vision_img = self.computer_vision_image(self.cv_image, resize=True)
        elements = self.detect_elements(computer_vision_img)

        match screen_show_mode:
            case "Computer_Vision":
                image_to_show = computer_vision_img
            case "Original":
                original_image = self.resize_image(self.cv_image)
                image_to_show = original_image
            case "Objects_Detecteds":
                original_image = self.resize_image(self.cv_image)
                image_to_show = self.draw_detected_objects(original_image, elements)
        
        return image_to_show
    
    def draw_detected_objects(self, img, elements):
        img = self.draw_and_log_elements(img, elements["dino"], "Dino", (0, 255, 0))  # Green
        img = self.draw_and_log_elements(img, elements["cactus"], "Cactus", (0, 0, 255))  # Red
        img = self.draw_and_log_elements(img, elements["fcking_prehistoric_birds"], "Fcking Prehistoric Birds", (0, 0, 192))
        return img# Dark Red
    
    def computer_vision_image(self, cv_image, resize=True):
        blurred_img = self.blur_image(cv_image)
        gray_img = self.convert_to_gray(blurred_img)
        sharp_img = self.apply_convolution(gray_img)
        if resize:
            sharp_img = self.resize_image(sharp_img)
        binary_img = self.threshold_image(sharp_img)
        
        return binary_img
        
    def draw_and_log_elements(self, img, elements, label, color):
        font = cv.FONT_HERSHEY_SIMPLEX
        font_scale = 0.3
        thickness = 1
        
        if elements:
            for element in elements:
                x, y, w, h = element
                cv.putText(img, label, (x, y - 10), font, font_scale, color, thickness)
                #print(f"{label} found at: x={x}, y={y}, width={w}, height={h}")
                cv.rectangle(img, (x, y), (x+w, y+h), color, 2)
        return img
        
    def apply_convolution(self, cv_image):
        filtered_image = cv.filter2D(cv_image, -1, self.kernel)
        return filtered_image
    
    def eightbit_image(self, cv_image):
        eightbit_array = np.uint8(np.absolute(cv_image))
        return eightbit_array
    
    def blur_image(self, cv_image):
        return cv.medianBlur(cv_image, 1)
    
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
            area = w * h
            
            if area > 300: #Small contours dosent count, better performace
                object_detected = ObjectDetected(contour, "Unknown")                
                
                if object_detected.is_dino():
                    is_new = True
                    for existing_dino in dinos:
                        if self.is_duplicate(existing_dino, object_detected):
                            is_new = False
                            break
                    if is_new:
                        dinos.append(object_detected.dimensions())
                        #cv.drawContours(self.computer_img, contour, 0, (0, 255, 0), 4)
                        
                elif object_detected.is_cactus():
                    cactus.append(object_detected.dimensions())
                    #cv.drawContours(self.computer_img, contour, 0, (255, 0, 0), 4)
                elif object_detected.is_fcking_prehistoric_birds():
                    fcking_prehistoric_birds.append(object_detected.dimensions())
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
        x, y, w, h = new_object.dimensions()
        if abs(x - ex) < threshold and abs(y - ey) < threshold:
            return True
        else:
            return False        
        
    def locate_game_region(self):
        computer_vision_image = self.computer_vision_image(self.cv_image, resize=False)
        croped_image = self.cv_image
        browser_bar = None
        image_height, image_width = computer_vision_image.shape
        
        contours, hierarchy = self.find_contours(computer_vision_image)
        
        for contour in contours:
            object_detected = ObjectDetected(contour, "Unknown")
            
            if object_detected.is_dino():
                if browser_bar is not None:
                    min_y = browser_bar.y
                else:
                    min_y = object_detected.y - object_detected.height() * 2
                    
                max_y = object_detected.y + object_detected.height()*2
                
                y_start = max(0, min_y) # Extend upwards
                y_end = min(image_height, max_y) # Extend downwards
                
                min_x = object_detected.x - object_detected.width()
                max_x = object_detected.x + object_detected.width() * 14
                
                x_start = max(0, min_x) # Extend to the left
                x_end = min(image_width, max_x)  # Extend to the right
                
                game_x = x_start
                game_y = y_start
                game_height = y_end - y_start
                game_width = x_end - x_start
                
                
                cv.rectangle(croped_image, (object_detected.x, object_detected.y), (object_detected.x+object_detected.w, object_detected.y+object_detected.h), (255, 0, 0), 2)
                croped_image = croped_image[y_start:y_end, x_start:x_end]
                cv.imshow("Game Region", croped_image)
                cv.waitKey(0)
                cv.destroyAllWindows()
                
                return game_x, game_y, game_height, game_width
            
            elif object_detected.lenght() >= image_width * 0.90:
                browser_bar = ObjectDetected(contour, "BrowserBar")
        
        return None