from read_image import readImage
from detect_features.in_range import get_mask_in_range
from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

image = readImage("C:\\ComputerVision\\images.jpg", 'HSV')

mask = get_mask_in_range(image, 'RBG', np.array([10, 0, 50]), np.array([18, 65, 100]))
plt.imshow(mask)
plt.show()