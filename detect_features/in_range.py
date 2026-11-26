import cv2 as cv
from cv2.typing import MatLike
from typing import cast

def get_mask_in_range(img:MatLike,format:str='BGR',lower:list=[0,0,0],upper:list=[0,0,0]):
    '''
        Calculate the mask for values in the given ranges.
    '''
    return cv.inRange(img, lower, upper)
