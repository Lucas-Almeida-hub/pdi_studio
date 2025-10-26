import cv2
import numpy as np

class HistogramModel:
    def __init__(self):
        pass
    
    def calculate_histogram(self, image):
        if image is None:
            return None
        
        # Calcula histograma para cada canal
        hist_b = cv2.calcHist([image], [0], None, [256], [0, 256])
        hist_g = cv2.calcHist([image], [1], None, [256], [0, 256])
        hist_r = cv2.calcHist([image], [2], None, [256], [0, 256])
        
        return hist_b.flatten(), hist_g.flatten(), hist_r.flatten()
    
    def adjust_brightness_contrast(self, image, brightness=0, contrast=1.0):
        if image is None:
            return None
        
        # Aplica ajuste: new_pixel = contrast * pixel + brightness
        adjusted = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
        return adjusted