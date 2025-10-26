import tkinter as tk
from views.menu_bar import MenuBar
from views.image_panel import ImagePanel
from views.control_panel import ControlPanel
from views.histogram_canvas import HistogramCanvas
from views.threshold_panel import ThresholdPanel
from views.edge_panel import EdgePanel
from views.custom_filter_panel import CustomFilterPanel

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        # Menu superior
        self.menu = MenuBar(self.root, controller)
        self.root.config(menu=self.menu.menubar)

        # Painéis
        self.image_panel = ImagePanel(self.root)
        self.image_panel.set_controller(controller)
        self.control_panel = ControlPanel(self.root)

        # Prioriza empacotar o painel de controle primeiro para reservar espaço do log
        self.control_panel.frame.pack(side="right", fill="y")
        self.image_panel.frame.pack(side="left", fill="both", expand=True)

    def display_image(self, image, is_original=False):
        self.image_panel.show_image(image, is_original)

    def log_action(self, text):
        self.control_panel.add_log(text)
    
    def show_histogram_window(self, controller):
        hist_window = tk.Toplevel(self.root)
        hist_window.title("Análise de Histograma")
        hist_window.geometry("800x500")
        hist_window.configure(bg="#222")
        
        self.histogram_canvas = HistogramCanvas(hist_window)
        self.histogram_canvas.frame.pack(fill="both", expand=True)
        self.histogram_canvas.set_apply_callback(lambda: controller.apply_brightness_contrast(
            self.histogram_canvas.brightness_var.get(),
            self.histogram_canvas.contrast_var.get()
        ))
        
        return self.histogram_canvas
    
    def show_threshold_window(self, controller):
        threshold_window = tk.Toplevel(self.root)
        threshold_window.title("Limiarização")
        threshold_window.geometry("400x400")
        threshold_window.configure(bg="#222")
        
        self.threshold_panel = ThresholdPanel(threshold_window)
        self.threshold_panel.frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Conectar callbacks
        self.threshold_panel.set_callbacks(
            lambda: controller.apply_global_threshold(self.threshold_panel.threshold_var.get()),
            lambda: controller.apply_multisegmented_threshold(self.threshold_panel.levels_var.get()),
            lambda: controller.apply_adaptive_threshold(self.threshold_panel.method_var.get()),
            lambda: controller.apply_otsu_threshold()
        )
        
        return self.threshold_panel
    
    def show_edge_window(self, controller):
        edge_window = tk.Toplevel(self.root)
        edge_window.title("Detecção de Bordas")
        edge_window.geometry("500x300")
        edge_window.configure(bg="#222")
        
        self.edge_panel = EdgePanel(edge_window)
        self.edge_panel.frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.edge_panel.set_callbacks(
            lambda: controller.apply_canny_edge(self.edge_panel.canny_low.get(), self.edge_panel.canny_high.get()),
            lambda: controller.apply_sobel_edge(),
            lambda: controller.apply_laplacian_edge()
        )
        
        return self.edge_panel
    
    def show_custom_filter_window(self, controller):
        filter_window = tk.Toplevel(self.root)
        filter_window.title("Filtros Customizados")
        filter_window.geometry("400x350")
        filter_window.configure(bg="#222")
        
        self.custom_filter_panel = CustomFilterPanel(filter_window)
        self.custom_filter_panel.frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.custom_filter_panel.set_callback(
            lambda: controller.apply_custom_filter(self.custom_filter_panel.get_kernel())
        )
        
        return self.custom_filter_panel
