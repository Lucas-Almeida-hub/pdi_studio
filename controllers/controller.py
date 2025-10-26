from tkinter import Tk, filedialog, messagebox
from models.model import Model
from views.view import View

class Controller:
    def __init__(self):
        self.root = Tk()
        self.root.title("PDI Studio - Sistema Interativo de Processamento de Imagens")
        self.root.geometry("1600x900")

        # Model
        self.model = Model()

        # View
        self.view = View(self.root, controller=self)

    # ========== Métodos principais ==========
    def run(self):
        self.root.mainloop()

    def open_image(self):
        path = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Arquivos de imagem", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        if path:
            image = self.model.load_image(path)
            self.view.display_image(image, is_original=True)
            operation = f"Imagem carregada: {path}"
            self.view.log_action(operation)
            self.model.add_operation_log(operation)

    def save_image(self):
        if self.model.image is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")]
        )
        if path:
            self.model.save_image(path)
            self.view.log_action(f"Imagem salva em: {path}")

    def apply_gray(self):
        result = self.model.convert_to_gray()
        self.view.display_image(result)
        operation = "Conversão para tons de cinza aplicada."
        self.view.log_action(operation)
        self.model.add_operation_log(operation)

    def apply_equalization(self):
        result = self.model.equalize_histogram()
        self.view.display_image(result)
        self.view.log_action("Equalização de histograma aplicada.")

    def reset_image(self):
        if self.model.original is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return
        result = self.model.reset_image()
        self.view.display_image(result)
        self.view.log_action("Imagem resetada para o estado original.")
    
    def show_pixel_info(self, x, y, is_original):
        rgb = self.model.get_pixel_value(x, y, is_original)
        if rgb:
            r, g, b = rgb
            img_type = "Original" if is_original else "Processada"
            self.view.log_action(f"{img_type} - Pixel ({x},{y}): R={r}, G={g}, B={b}")

    def convert_rgba(self):
        result = self.model.convert_to_rgba()
        self.view.display_image(result)
        self.view.log_action("Conversão para RGBA aplicada.")

    def convert_hsv(self):
        result = self.model.convert_to_hsv()
        self.view.display_image(result)
        self.view.log_action("Conversão para HSV aplicada.")

    def convert_lab(self):
        result = self.model.convert_to_lab()
        self.view.display_image(result)
        self.view.log_action("Conversão para LAB aplicada.")

    def convert_cmyk(self):
        result = self.model.convert_to_cmyk()
        self.view.display_image(result)
        self.view.log_action("Conversão para CMYK aplicada.")
    
    def open_histogram(self):
        if self.model.image is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return
        
        self.histogram_canvas = self.view.show_histogram_window(self)
        self.update_histogram()
    
    def update_histogram(self):
        if hasattr(self, 'histogram_canvas'):
            hist_original = self.model.get_histogram(is_original=True)
            hist_processed = self.model.get_histogram(is_original=False)
            self.histogram_canvas.plot_histograms(hist_original, hist_processed)
    
    def apply_brightness_contrast(self, brightness, contrast):
        result = self.model.adjust_brightness_contrast(brightness, contrast)
        self.view.display_image(result)
        self.view.log_action(f"Brilho: {brightness}, Contraste: {contrast:.1f} aplicados.")
        self.update_histogram()
    
    def open_threshold(self):
        if self.model.image is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return
        
        self.threshold_panel = self.view.show_threshold_window(self)
    
    def apply_global_threshold(self, threshold_value):
        result = self.model.apply_global_threshold(threshold_value)
        self.view.display_image(result)
        self.view.log_action(f"Limiarização global aplicada (valor: {threshold_value}).")
        if hasattr(self, 'histogram_canvas'):
            self.update_histogram()
    
    def apply_otsu_threshold(self):
        result, threshold_value = self.model.apply_otsu_threshold()
        self.view.display_image(result)
        self.view.log_action(f"Limiarização Otsu aplicada (valor calculado: {threshold_value:.1f}).")
        if hasattr(self, 'threshold_panel'):
            self.threshold_panel.update_otsu_value(threshold_value)
        if hasattr(self, 'histogram_canvas'):
            self.update_histogram()
    
    def apply_adaptive_threshold(self, method):
        result = self.model.apply_adaptive_threshold(method)
        self.view.display_image(result)
        self.view.log_action(f"Limiarização adaptativa ({method}) aplicada.")
        if hasattr(self, 'histogram_canvas'):
            self.update_histogram()
    
    def apply_multisegmented_threshold(self, levels):
        result = self.model.apply_multisegmented_threshold(levels)
        self.view.display_image(result)
        operation = f"Limiarização multissegmentada ({levels} níveis) aplicada."
        self.view.log_action(operation)
        self.model.add_operation_log(operation)
        if hasattr(self, 'histogram_canvas'):
            self.update_histogram()
    
    def open_edges(self):
        if self.model.image is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return
        self.edge_panel = self.view.show_edge_window(self)
    
    def apply_canny_edge(self, low_threshold, high_threshold):
        result = self.model.apply_canny_edge(low_threshold, high_threshold)
        self.view.display_image(result)
        operation = f"Detecção de bordas Canny (min:{low_threshold}, max:{high_threshold}) aplicada."
        self.view.log_action(operation)
        self.model.add_operation_log(operation)
        if hasattr(self, 'histogram_canvas'):
            self.update_histogram()
    
    def apply_sobel_edge(self):
        result = self.model.apply_sobel_edge()
        self.view.display_image(result)
        operation = "Detecção de bordas Sobel aplicada."
        self.view.log_action(operation)
        self.model.add_operation_log(operation)
        if hasattr(self, 'histogram_canvas'):
            self.update_histogram()
    
    def apply_laplacian_edge(self):
        result = self.model.apply_laplacian_edge()
        self.view.display_image(result)
        operation = "Detecção de bordas Laplaciano aplicada."
        self.view.log_action(operation)
        self.model.add_operation_log(operation)
        if hasattr(self, 'histogram_canvas'):
            self.update_histogram()
    
    def open_custom_filter(self):
        if self.model.image is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return
        self.custom_filter_panel = self.view.show_custom_filter_window(self)
    
    def apply_custom_filter(self, kernel):
        result = self.model.apply_custom_filter(kernel)
        self.view.display_image(result)
        operation = f"Filtro customizado aplicado: {kernel.tolist()}"
        self.view.log_action("Filtro customizado aplicado.")
        self.model.add_operation_log(operation)
        if hasattr(self, 'histogram_canvas'):
            self.update_histogram()
    
    def generate_report(self):
        if self.model.original is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada.")
            return
        
        from tkinter import filedialog
        path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF", "*.pdf")],
            title="Salvar Relatório"
        )
        
        if path:
            success = self.model.generate_report(path)
            if success:
                self.view.log_action(f"Relatório PDF gerado: {path}")
                messagebox.showinfo("Sucesso", "Relatório PDF gerado com sucesso!")
            else:
                messagebox.showerror("Erro", "Erro ao gerar relatório. Instale: pip install reportlab")
