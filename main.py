from screen_capture.screen_capture import DinoGameWithScreenCapture
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
        
        game.screen_capture()
        
        
        key = cv.waitKey(1) #Tá crashando ao apertar q
        if key == ord('q'):
            dinogui.finish()
            game.close()
            break
        
        elapsed_time = time.time() - t0
        average_fps = (n_frames / elapsed_time)
        dinogui.refresh(average_fps)
        n_frames += 1
        
        
        #game.keep_open()  # Keep the browser open is crashing esse trem