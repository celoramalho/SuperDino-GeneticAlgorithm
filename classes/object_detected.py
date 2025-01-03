import cv2 as cv
import numpy as np
import os

class ObjectDetected:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    PARENT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
    reference_contours = {"dino" : [], "cactus" : [], "fcking_prehistoric_bird" : []}
    #reference_descriptors = {"dino" : [], "cactus" : [], "fcking_prehistoric_bird" : []}	
    #reference_keypoints = {"dino" : [], "cactus" : [], "fcking_prehistoric_bird" : []}
    
    #orb = cv.ORB_create()
    
    reference_images = {
        "dino": [os.path.join(PARENT_DIR, "img", "dino_up.png"), os.path.join(PARENT_DIR, "img", "original_dino.png")],
        "cactus": [os.path.join(PARENT_DIR, "img", "cactus-1.png")],
        "fcking_prehistoric_bird": [os.path.join(PARENT_DIR, "img", "prehistoric_bird.png")]
    }
    binary_images = []

    min_area = 200
    min_perimeter = 50
    similarity_threshold = 0.15
    #good_matches_threshold = 5

    @classmethod
    def get_contour_reference_objects(cls, image):
        img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        blurred_image = cv.medianBlur(img_gray, 1)
        kernel_sharpening = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        img_sharpened = cv.filter2D(blurred_image, -1, kernel_sharpening)
        eightbit = np.uint8(np.absolute(img_sharpened))#8-bit vallues within range 0 to 255

        _, binary = cv.threshold(eightbit, 10, 255, cv.THRESH_BINARY)
        
        contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)    
        if contours:
            object_contour = contours[0]
            cls.binary_images.append(binary)
            return object_contour
        else:
            raise ValueError("No contour found in the image.")

    @classmethod
    def initialize_reference_contours(cls):
        print("Initializing reference contours...")
        #orb = cls.orb
        """Carrega e processa as imagens de referência, armazenando seus contornos."""
        for name, paths in cls.reference_images.items():
            for path in paths:
                print(f"Loading reference image: {path}")
                cv_image = cv.imread(path)
                if cv_image is not None:
                    contour = cls.get_contour_reference_objects(cv_image)
                    #contour_clean = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
                    cls.reference_contours[name].append(contour)
                    
                    #keypoints, descriptors = orb.detectAndCompute(cv_image, None)
                    
                    #cls.reference_keypoints[name].append(keypoints)
                    #cls.reference_descriptors[name].append(descriptors)
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
    
    def location(self):
        return (self.x, self.y)
    
    def is_object(self, object_type):

        # Size Matching
        if self.area < self.min_area:
            return False

        # Shape Matching
        min_similarity = float("inf")
        for contour in ObjectDetected.reference_contours[object_type]:
            similarity = cv.matchShapes(contour, self.contour, cv.CONTOURS_MATCH_I1, 0)
            min_similarity = min(min_similarity, similarity)

        if min_similarity > ObjectDetected.similarity_threshold:
            return False
        else:
            print(f"{object_type} Similarity: {min_similarity}")
            self.label = object_type
            return True

        # Feature Matching
        #blank_image = np.zeros((self.h, self.w), dtype=np.uint8)
        #adjusted_contour = self.contour - [self.x, self.y]
        #blank_image = cv.drawContours(blank_image, [adjusted_contour], -1, 255, thickness=cv.FILLED)
        #cv.imshow("Blank_Image", blank_image)
        #cv.waitKey(0)
        #cv.destroyAllWindows()
        
        
        #for ref_keypoints, ref_descriptors in zip(ObjectDetected.reference_keypoints[object_type], ObjectDetected.reference_descriptors[object_type]):
        #    keypoints, descriptors = ObjectDetected.orb.detectAndCompute(blank_image, None)
        #    
        #    print(f"descriptors: {descriptors}")
        #    print(f"ref_descriptors: {ref_descriptors}")
            
            #if descriptors is not None and ref_descriptors is not None:
            #    bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=False)
            #    matches = bf.knnMatch(ref_descriptors, descriptors, k=2)
            #    good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]

            #    ref_image = cv.imread(ObjectDetected.reference_images[object_type][0])
            #    matched_image = cv.drawMatches(ref_image, ref_keypoints, blank_image, keypoints, matches[:10], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            #    cv.imshow("Matches", matched_image)
            #    cv.waitKey(0)
            #    cv.destroyAllWindows()
            #    
            #    if len(good_matches) > ObjectDetected.good_matches_threshold:
            #        self.label = object_type
            #        return True
        return False

    
    def show_reference_images():
        images = {}
        for name, paths in ObjectDetected.reference_images.items():
            for path in paths:
                images[name] = cv.imread(path)
            
                cv.imshow(name, images[name])
                cv.waitKey(0)
                cv.destroyAllWindows()
             
        list(images.keys())
    
    def show_reference_images_computer_vision():
        for image in ObjectDetected.binary_images:
            cv.imshow("binary", image)
            cv.waitKey(0)
            cv.destroyAllWindows()
    
    """
    def is_dino(self): #bidimensional (2D)
        min_similarity = 9999
        
        if self.area < self.min_area:
            return False

        # Shape Matching
        for dino_contour in ObjectDetected.reference_contours["dino"]:        
            similarity = cv.matchShapes(dino_contour, self.contour, cv.CONTOURS_MATCH_I1, 0)
            if similarity < min_similarity:
                min_similarity = similarity
            #print(f"similarity: {similarity}, position: {self.x}, {self.y}")
            
        if min_similarity > 0.5:
            return False
        
        #Feature Matching
        for ref_keypoints, ref_descriptors in zip(ObjectDetected.reference_keypoints["dino"], ObjectDetected.reference_descriptors["dino"]):    
            
            mask = np.zeros_like(self.contour, dtype=np.uint8)
            cv.drawContours(mask, [self.contour], -1, 255, thickness=cv.FILLED)
            keypoints, descriptors = self.orb.detectAndCompute(mask, None)
            
            if descriptors is not None and ref_descriptors is not None:
                matches = self.orb.match(ref_descriptors, descriptors)
                matches = sorted(matches, key=lambda x: x.distance)
                good_matches = [m for m in matches if m.distance < 50]
                
                if len(good_matches) > 10:
                                       
                    print(f"Dino similarity: {min_similarity}, position: {self.x}, {self.y}")
                    self.label = "dino"
                    return True
                
        return False
        
    def is_cactus(self): #bidimensional (2D)
        min_similarity = 9999
        for contour in ObjectDetected.reference_contours["cactus"]:        
            similarity = cv.matchShapes(contour, self.contour, cv.CONTOURS_MATCH_I1, 0)
            if similarity < min_similarity:
                min_similarity = similarity
        
        if self.area >= self.min_area:
            if 20 < self.w < 60 and 20 < self.h < 60 and 0.5 < self.aspect_ratio < 1.5:
                #print(f"similarity: {similarity}, position: {self.x}, {self.y}")
                self.label = "cactus"
                return False
            else:
                return False
    
    def is_fcking_prehistoric_bird(self): #bidimensional (2D)
        min_similarity = 9999
        for contour in ObjectDetected.reference_contours["fcking_prehistoric_bird"]:        
            similarity = cv.matchShapes(contour, self.contour, cv.CONTOURS_MATCH_I1, 0)
            if similarity < min_similarity:
                min_similarity = similarity
        
        if self.area >= self.min_area:
            if similarity < 0.15:
                #print(f"similarity: {similarity}, position: {self.x}, {self.y}")
                self.label = "pterodactyl"
                return True
            else:
                return False


"""

