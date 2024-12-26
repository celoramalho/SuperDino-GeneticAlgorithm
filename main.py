from screen_capture.screen_capture import DinoGameWithScreenCapture
from screen_capture.screenshot import Screenshot
from gui_terminal.dino_terminal_gui import DinoTerminalGui


import cv2 as cv
import time
# Usar a classe
# Example usage

t0 = time.time()
n_frames = 1

dinogui = DinoTerminalGui(13)
if __name__ == "__main__":
    game = DinoGameWithScreenCapture()
    game.open_game()
    
    while True:
        
        screenshot_array = Screenshot(game.screen_capture()) # NumPy array
        screenshot_array.show_screenshot()
        screenshot_array.process()
        
        
        key = cv.waitKey(1) #Tá crashando ao apertar q
        if key == ord('q'):
            dinogui.finish()
            game.close()
            break
        
        elapsed_time = time.time() - t0
        average_fps = (n_frames / elapsed_time)
        dinogui.refresh(average_fps)
        print(f"NumPy Array Shape(Height, Width): {screenshot_array.screenshot_array.shape}") #screenshot_array.screenshot_array.shape)
        print(f"Background Color: {screenshot_array.background_color}")
        #screenshot_array.print_pixels_ocurrences()
        n_frames += 1


        
        
        #game.keep_open()  # Keep the browser open is crashing esse trem