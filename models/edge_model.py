import cv2
import numpy as np

class EdgeModel:
    def __init__(self):
        pass
    
    def canny_edge(self, image, low_threshold=50, high_threshold=150):
        if image is None:
            return None
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, low_threshold, high_threshold)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    def sobel_edge(self, image, ksize=3):
        if image is None:
            return None
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
        sobel = np.sqrt(sobelx**2 + sobely**2)
        sobel = np.uint8(np.clip(sobel, 0, 255))
        return cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR)
    
    def laplacian_edge(self, image, ksize=3):
        if image is None:
            return None
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
        laplacian = np.uint8(np.absolute(laplacian))
        return cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR)