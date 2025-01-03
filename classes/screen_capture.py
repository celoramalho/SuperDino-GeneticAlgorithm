import mss
from classes.dino_game_selenium import DinoGameSelenium
from classes.image_processing import ImageProcessing
from classes.screenshot import Screenshot
from classes.object_detected import ObjectDetected
import numpy as np

class DinoGameWithScreenCapture(DinoGameSelenium):
    
    def start(self):
        super().__init__()
        super().open()
        ObjectDetected.initialize_reference_contours()
        #ObjectDetected.show_reference_images_computer_vision()#ObjectDetected.show_reference_images()
        self.chrome_region = self.get_chrome_window_region()
        #print(f"Chrome Region: {self.chrome_region}")
        self.game_region = self.find_game_region()
        
    
    def get_chrome_window_region(self):
        rect = self.driver.get_window_rect()
        return {
            "top": rect["y"],
            "left": rect["x"],
            "width": rect["width"],
            "height": rect["height"]
        }                
    
    def capture_window(self, region):
        with mss.mss() as sct:
            screenshot = sct.grab(region)
            return np.array(screenshot) # Convert to NumPy array

    def find_game_region(self):
        np_img = self.capture_window(self.chrome_region)
        chrome_screenshot = Screenshot(np_img)
        game_region = chrome_screenshot.locate_game_region()
        if game_region is None:
            return False
        else:
            #print(f"Game Region found???: {game_region}")
            game_x, game_y, game_height, game_width = game_region        

            return {
                "top": game_y + self.chrome_region["top"],
                "left": game_x + self.chrome_region["left"],
                "width": game_width,
                "height": game_height
            }
        
    def screen_capture(self):
        new_region = self.get_chrome_window_region()
        if self.chrome_region != new_region:
            #print("Chrome Region changed.")
            self.chrome_region = new_region
            self.game_region = self.find_game_region()
            #print(f"Game Region: {self.game_region}")
        
        region = self.game_region if self.game_region else self.chrome_region
        print(f"Region: {region}")
        np_img = self.capture_window(region)
        return np_img 