import mss
from classes.dino_game_selenium import DinoGameSelenium
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
        region = self.get_chrome_window_region() # Define this here inside the loop? Se a pessoa mudar a dimensão da janela
        np_img = self.capture_chrome_window(region)
        return np_img