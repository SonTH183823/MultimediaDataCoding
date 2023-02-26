import cv2
import numpy as np
import os
# from . import zigzag
# from . import QuantizationTables
# from . import RunLengthCoding as RLE
# from . import logStatus
import time
# from . import huffman
path = r'C:\Users\banba\Downloads\Multimedia-Data-Coding\testImg\anh_demo.jpg'
img = cv2.imread(path)
print(img.shape[:2])
print(img.size)
# cv2.imshow('image', img)
# cv2.waitKey()
cv2.imwrite('abc.jpg', img)