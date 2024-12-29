import mss
from classes.dino_game_selenium import DinoGameSelenium
#from PIL import Image, ImageGrab
#import pyautogui
import numpy as np
#https://www.youtube.com/watch?v=SWgQNWf1ICA&t=91s

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
        #gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #BGR2 # Convert RGB to BGR color; try black and white
        #already BGR img?
        #gray_img_resized = cv.resize(gray_img, (0, 0), fx=0.5, fy=0.5)#fx=0.5, fy=0.5)
        
        #Testando e vendo a saida
        #numpy_to_list = small.tolist()
        #with open ('numpy_array_test.json', 'w') as file:
        #    json.dump(numpy_to_list, file)

        #print(f"NumPy Array Lenght: {small.shape}")
        #print(f"Image type in screen_capture method: {type(np_img)}")
        return np_img