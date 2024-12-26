import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class ConvolutionKernel:
    Laplacian = np.array([[0, 1, 0], 
                      [1, -4, 1], 
                      [0, 1, 0]])
    Sobel_X = np.array([[-1, 0, 1], 
                    [-2, 0, 2], 
                    [-1, 0, 1]])

    Sobel_Y = np.array([[-1, -2, -1], 
                        [ 0,  0,  0], 
                        [ 1,  2,  1]])
    Emboss = np.array([[-2, -1,  0],
                    [-1,  1,  1],
                    [ 0,  1,  2]])
    Kirsch = np.array([[ 5,  5,  5], 
                    [-3,  0, -3], 
                    [-3, -3, -3]])
    Prewitt_X = np.array([[-1, 0, 1],
                        [-1, 0, 1],
                        [-1, 0, 1]])
    Prewitt_Y = np.array([[-1, -1, -1], 
                        [ 0,  0,  0], 
                        [ 1,  1,  1]])
    kernels = {
        "Laplacian": Laplacian,
        "Sobel X": Sobel_X,
        "Sobel Y": Sobel_Y,
        "Emboss": Emboss,
        "Kirsch Compass": Kirsch,
        "Prewitt X": Prewitt_X,
        "Prewitt Y": Prewitt_Y
    }
    