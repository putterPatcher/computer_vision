import cv2 as cv
from cv2.typing import MatLike

def readImage(path:str,format:str='BGR')->MatLike|None:
    if format=='BGR':return cv.imread(path);
    if format=='RGB':return cv.imread(path,cv.IMREAD_COLOR_RGB);
    if format=='grayscale':image=cv.imread(path);return cv.cvtColor(image,cv.COLOR_BGR2GRAY);
    if format=='HSV':image=cv.imread(path);return cv.cvtColor(image,cv.COLOR_BGR2HSV);
