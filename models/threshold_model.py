import cv2
import numpy as np

class ThresholdModel:
    def __init__(self):
        pass
    
    def global_threshold(self, image, threshold_value=127):
        """Limiarização global com valor fixo"""
        if image is None:
            return None
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
        return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    
    def otsu_threshold(self, image):
        """Limiarização automática usando método de Otsu"""
        if image is None:
            return None
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        threshold_value, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR), threshold_value
    
    def adaptive_threshold(self, image, method='mean', block_size=11, c=2):
        """Limiarização adaptativa"""
        if image is None:
            return None
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        adaptive_method = cv2.ADAPTIVE_THRESH_MEAN_C if method == 'mean' else cv2.ADAPTIVE_THRESH_GAUSSIAN_C
        binary = cv2.adaptiveThreshold(gray, 255, adaptive_method, cv2.THRESH_BINARY, block_size, c)
        return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    
    def multisegmented_threshold(self, image, levels=2):
        """Limiarização multissegmentada (2, 4, 8 ou 16 tons)"""
        if image is None:
            return None
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Calcula os valores de limiar baseado no número de níveis
        step = 256 // levels
        segmented = np.zeros_like(gray)
        
        for i in range(levels):
            lower = i * step
            upper = (i + 1) * step if i < levels - 1 else 256
            mask = (gray >= lower) & (gray < upper)
            segmented[mask] = i * (255 // (levels - 1)) if levels > 1 else 255
        
        return cv2.cvtColor(segmented, cv2.COLOR_GRAY2BGR)