from classes.screen_capture import DinoGameWithScreenCapture
from classes.screenshot import Screenshot
from classes.dino_terminal_gui import DinoTerminalGui


import cv2 as cv
import time
# Usar a classe
# Example usage

t0 = time.time()
n_frames = 1
kernel = "Laplacian" # Laplacian, Prewitt X, Prewitt Y, Emboss, Kirsch Compass, Sobel X, Sobel Y


dinogui = DinoTerminalGui(13)
if __name__ == "__main__":
    game = DinoGameWithScreenCapture()
    game.open_game()
    
    while True:
        
        np_screenshot = Screenshot(game.screen_capture()) # NumPy array
        processed_np_img = np_screenshot.process_img()
        #print(type(processed_np_img))
        processed_np_img.show()
        
        key = cv.waitKey(1)
        if key == ord('q'):
            print("Exiting...")
            break
        
        elapsed_time = time.time() - t0
        average_fps = (n_frames / elapsed_time)
        dinogui.refresh(average_fps)
        n_frames += 1


        
        
        #game.keep_open()  # Keep the browser open is crashing esse trem