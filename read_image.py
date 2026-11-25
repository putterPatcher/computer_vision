import cv2 as cv
from cv2.typing import MatLike

def readImage(path:str,format:str='BGR')->MatLike|None:
    if format=='BGR':return cv.imread(path);
    if format=='RBG':return cv.imread(path,cv.COLOR_BGR2RGB);
    if format=='grayscale':return cv.imread(path,cv.COLOR_BGR2GRAY);
    if format=='HSV':return cv.imread(path,cv.COLOR_BGR2HSV);

