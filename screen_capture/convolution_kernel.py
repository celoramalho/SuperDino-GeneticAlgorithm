import cv2 as cv
import numpy as np
#import matplotlib.pyplot as plt

class ConvolutionKernel:
    kernels = {
        "Laplacian": np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]),
        "Sobel X": np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]),
        "Sobel Y": np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]),
        "Emboss": np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]),
        "Kirsch Compass": np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]]),
        "Prewitt X": np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]),
        "Prewitt Y": np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]]),
    }

    def __init__(self, kernel_name):
        if kernel_name not in self.kernels:
            raise ValueError(f"Kernel '{kernel_name}' not found. Choose between: {list(self.kernels.keys())}")
        self.kernel = self.kernels[kernel_name]

    def apply_convolution(self, image):
        blurred_image = image#cv.GaussianBlur(image, (3, 3), 0)
        filtered_image = cv.filter2D(blurred_image, -1, self.kernel)
        eightbit_array = np.uint8(np.absolute(filtered_image))
        _, binary = cv.threshold(eightbit_array, 30, 255, cv.THRESH_BINARY) #Convert to Binary
        return binary 