from read_image import readImage
from detect_features.in_range import get_mask_in_range
from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

image = readImage(".\\images (1).jpg", 'HSV')

plt.imshow(image)
plt.show()

mask = get_mask_in_range(image, 'RBG', np.array([0, 0, 0]), np.array([20, 255, 100]))
plt.imshow(mask)
plt.show()