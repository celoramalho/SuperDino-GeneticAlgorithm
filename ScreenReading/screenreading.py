import mss
from PIL import Image, ImageGrab
import pyautogui

import cv2 as cv
import numpy as np
import time
#https://www.youtube.com/watch?v=SWgQNWf1ICA&t=91s

def get_chrome_window():
    # Localiza a janela do Chrome pelo título
    for window in gw.getAllWindows():
        if "Chrome" in window.title:
            return window
    return None



class DinoGameWithCapture:
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

    def start_screen_capture(self):
        while True:
            region = self.get_chrome_window_region() # Define this here inside the loop? Se a pessoa mudar a dimensão da janela
            img = self.capture_chrome_window(region)
            #gray_img = cv2.cvtColor(img, cv.COLOR_BGR2GRAY) #BGR2 # Convert RGB to BGR color
            #already BGR img?
            small = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
            cv.imshow("Computer Vision", small)
            
            key = cv.waitKey(1)
            if key == ord('q'):
                break