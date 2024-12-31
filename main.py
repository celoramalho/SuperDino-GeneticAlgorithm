from classes.screen_capture import DinoGameWithScreenCapture
from classes.screenshot import Screenshot
from classes.dino_terminal_gui import DinoTerminalGui


import cv2 as cv
import time
import numpy as np
# Usar a classe
# Example usage

t0 = time.time()
n_frames = 1
kernel = "Laplacian" # Laplacian, Prewitt X, Prewitt Y, Emboss, Kirsch Compass, Sobel X, Sobel Y



def get_contour_reference_objects(image):
        img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        blurred_image = cv.medianBlur(img_gray, 1)
        kernel_sharpening = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        img_sharpened = cv.filter2D(blurred_image, -1, kernel_sharpening)
        eightbit = np.uint8(np.absolute(img_sharpened))#8-bit vallues within range 0 to 255

        _, binary = cv.threshold(eightbit, 30, 255, cv.THRESH_BINARY)
        
        contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)     
        object_contour = contours[0]
        
        return object_contour
def load_reference_contours(reference_images):
    reference_contours = {}
    for reference in reference_images:
        cv_image = cv.imread(reference_images[reference])
        if cv_image is not None:
            reference_contours[reference] = get_contour_reference_objects(cv_image)
        else:
            raise FileNotFoundError(f"Error: Image {reference_images[reference]} not found or could not be loaded.")
    return reference_contours


reference_images = {"dino_up": "img/dino_up.png",
                                 "cactus": "img/cactus-1.png",
                                 "fcking_prehistoric_birds": "img/prehistoric_bird.png"}
reference_contours = load_reference_contours(reference_images)



dinogui = DinoTerminalGui(13)
if __name__ == "__main__":
    game = DinoGameWithScreenCapture()
    game.open_game()
    
    while True:
        
        np_screenshot = Screenshot(game.screen_capture(reference_contours), reference_contours) # NumPy array
        processed_np_img = np_screenshot.process_img()
        #print(type(processed_np_img))
        processed_np_img.show(mode = 'Objects_Detecteds')
        
        key = cv.waitKey(1)
        if key == ord('q'):
            print("Exiting...")
            break
        
        elapsed_time = time.time() - t0
        average_fps = (n_frames / elapsed_time)
        dinogui.refresh(average_fps)
        n_frames += 1

        #game.keep_open()  # Keep the browser open is crashing esse trem