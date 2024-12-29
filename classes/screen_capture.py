import mss
from classes.dino_game_selenium import DinoGameSelenium
from classes.image_processing import ImageProcessing
from classes.screenshot import Screenshot
import numpy as np

class DinoGameWithScreenCapture(DinoGameSelenium):

    def get_chrome_window_region(self):
        rect = self.driver.get_window_rect()
        return {
            "top": rect["y"],
            "left": rect["x"],
            "width": rect["width"],
            "height": rect["height"]
        }                
    
    def capture_chrome_window(self, region):
        with mss.mss() as sct:
            screenshot = sct.grab(region)
            return np.array(screenshot) # Convert to NumPy array

    def screen_capture(self):
        chrome_region = self.get_chrome_window_region() # Define this here inside the loop? Se a pessoa mudar a dimensão da janela
        np_img = self.capture_chrome_window(chrome_region)
        chrome_screenshot = Screenshot(np_img)
        game_region_screenshot = chrome_screenshot.game_region()
        return game_region_screenshot