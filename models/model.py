import cv2
from PIL import Image, ImageTk
import numpy as np
from models.histogram_model import HistogramModel
from models.threshold_model import ThresholdModel
from models.edge_model import EdgeModel
from models.report_model import ReportModel

class Model:
    def __init__(self):
        self.image = None
        self.original = None
        self.original_tk = None
        self.histogram_model = HistogramModel()
        self.threshold_model = ThresholdModel()
        self.edge_model = EdgeModel()
        self.report_model = ReportModel()
        self.operations_log = []

    def load_image(self, path):
        self.image = cv2.imread(path)
        self.original = self.image.copy()
        self.original_tk = self.to_tk_image(self.image)
        self.operations_log = []  # Reset log para nova imagem
        return self.original_tk

    def save_image(self, path):
        if self.image is not None:
            cv2.imwrite(path, self.image)

    def reset_image(self):
        if self.original is not None:
            self.image = self.original.copy()
            return self.to_tk_image(self.image)

    # ========== Operações de PDI ==========
    def convert_to_gray(self):
        if self.image is None:
            return None
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        return self.to_tk_image(self.image)

    def equalize_histogram(self):
        if self.image is None:
            return None
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        equalized = cv2.equalizeHist(gray)
        self.image = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)
        return self.to_tk_image(self.image)

    def convert_to_rgba(self):
        if self.image is None:
            return None
        rgba = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGBA)
        # Adiciona canal alpha com valor 255 (opaco)
        alpha = np.full((rgba.shape[0], rgba.shape[1], 1), 255, dtype=np.uint8)
        rgba = np.concatenate([rgba[:,:,:3], alpha], axis=2)
        # Para visualização, usa apenas RGB
        self.image = rgba[:,:,:3]
        self.image = cv2.cvtColor(self.image, cv2.COLOR_RGB2BGR)
        return self.to_tk_image(self.image)

    def convert_to_hsv(self):
        if self.image is None:
            return None
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        # Mapeia HSV para RGB para visualização
        h, s, v = cv2.split(hsv)
        # Normaliza H para 0-255 para melhor visualização
        h_norm = (h.astype(np.float32) * 255 / 179).astype(np.uint8)
        hsv_visual = cv2.merge([h_norm, s, v])
        self.image = cv2.cvtColor(hsv_visual, cv2.COLOR_RGB2BGR)
        return self.to_tk_image(self.image)

    def convert_to_lab(self):
        if self.image is None:
            return None
        lab = cv2.cvtColor(self.image, cv2.COLOR_BGR2LAB)
        # Normaliza LAB para visualização RGB
        l, a, b = cv2.split(lab)
        # Ajusta A e B de [-128,127] para [0,255]
        a_norm = cv2.add(a, 128)
        b_norm = cv2.add(b, 128)
        lab_visual = cv2.merge([l, a_norm, b_norm])
        self.image = cv2.cvtColor(lab_visual, cv2.COLOR_RGB2BGR)
        return self.to_tk_image(self.image)

    def convert_to_cmyk(self):
        if self.image is None:
            return None
        rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        rgb_norm = rgb.astype(np.float32) / 255.0
        k = 1 - np.max(rgb_norm, axis=2)
        c = (1 - rgb_norm[:,:,0] - k) / (1 - k + 1e-10)
        m = (1 - rgb_norm[:,:,1] - k) / (1 - k + 1e-10)
        y = (1 - rgb_norm[:,:,2] - k) / (1 - k + 1e-10)
        cmyk = np.stack([c, m, y], axis=2)
        cmyk_rgb = (cmyk * 255).astype(np.uint8)
        self.image = cv2.cvtColor(cmyk_rgb, cv2.COLOR_RGB2BGR)
        return self.to_tk_image(self.image)

    # ========== Conversão ==========
    def to_tk_image(self, cv_image, max_width=400, max_height=400):
        rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(rgb)
        
        # Redimensiona mantendo proporção
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    
    def get_pixel_value(self, x, y, is_original=False):
        img = self.original if is_original else self.image
        if img is not None and 0 <= y < img.shape[0] and 0 <= x < img.shape[1]:
            b, g, r = img[y, x]
            return int(r), int(g), int(b)
        return None
    
    def get_histogram(self, is_original=False):
        img = self.original if is_original else self.image
        return self.histogram_model.calculate_histogram(img)
    
    def adjust_brightness_contrast(self, brightness, contrast):
        if self.image is None:
            return None
        adjusted = self.histogram_model.adjust_brightness_contrast(self.image, brightness, contrast)
        self.image = adjusted
        return self.to_tk_image(self.image)
    
    def apply_global_threshold(self, threshold_value):
        if self.image is None:
            return None
        result = self.threshold_model.global_threshold(self.image, threshold_value)
        self.image = result
        return self.to_tk_image(self.image)
    
    def apply_otsu_threshold(self):
        if self.image is None:
            return None, 0
        result, threshold_value = self.threshold_model.otsu_threshold(self.image)
        self.image = result
        return self.to_tk_image(self.image), threshold_value
    
    def apply_adaptive_threshold(self, method):
        if self.image is None:
            return None
        result = self.threshold_model.adaptive_threshold(self.image, method)
        self.image = result
        return self.to_tk_image(self.image)
    
    def apply_multisegmented_threshold(self, levels):
        if self.image is None:
            return None
        result = self.threshold_model.multisegmented_threshold(self.image, levels)
        self.image = result
        return self.to_tk_image(self.image)
    
    def apply_canny_edge(self, low_threshold, high_threshold):
        if self.image is None:
            return None
        result = self.edge_model.canny_edge(self.image, low_threshold, high_threshold)
        self.image = result
        return self.to_tk_image(self.image)
    
    def apply_sobel_edge(self):
        if self.image is None:
            return None
        result = self.edge_model.sobel_edge(self.image)
        self.image = result
        return self.to_tk_image(self.image)
    
    def apply_laplacian_edge(self):
        if self.image is None:
            return None
        result = self.edge_model.laplacian_edge(self.image)
        self.image = result
        return self.to_tk_image(self.image)
    
    def apply_custom_filter(self, kernel):
        if self.image is None:
            return None
        result = cv2.filter2D(self.image, -1, kernel)
        self.image = result
        return self.to_tk_image(self.image)
    
    def generate_report(self, output_path):
        if self.original is None or self.image is None:
            return False
        try:
            self.report_model.generate_report(self.original, self.image, self.operations_log, output_path)
            return True
        except:
            return False
    
    def add_operation_log(self, operation):
        self.operations_log.append(operation)
