import tkinter as tk
from tkinter import Label, Scrollbar, Canvas

class ImagePanel:
    def __init__(self, root):
        self.frame = tk.Frame(root, bg="#222")
        
        # Frame para imagem original
        self.original_frame = tk.Frame(self.frame, bg="#222")
        self.original_frame.pack(side="left", fill="both", expand=True)
        tk.Label(self.original_frame, text="Original", bg="#222", fg="white", font=("Arial", 10, "bold")).pack()
        
        # Canvas com scrollbars para original
        self.original_canvas = Canvas(self.original_frame, bg="#222", highlightthickness=0)
        self.original_canvas.pack(fill="both", expand=True)
        self.original_label = Label(self.original_canvas, bg="#222")
        self.original_canvas.create_window(0, 0, anchor="nw", window=self.original_label)
        
        # Frame para imagem processada
        self.processed_frame = tk.Frame(self.frame, bg="#222")
        self.processed_frame.pack(side="right", fill="both", expand=True)
        tk.Label(self.processed_frame, text="Processada", bg="#222", fg="white", font=("Arial", 10, "bold")).pack()
        
        # Canvas com scrollbars para processada
        self.processed_canvas = Canvas(self.processed_frame, bg="#222", highlightthickness=0)
        self.processed_canvas.pack(fill="both", expand=True)
        self.processed_label = Label(self.processed_canvas, bg="#222")
        self.processed_canvas.create_window(0, 0, anchor="nw", window=self.processed_label)
        
        self.original_image = None

    def show_image(self, image, is_original=False):
        if is_original:
            self.original_image = image
            self.original_label.config(image=image)
            self.original_label.image = image
            self.original_label.bind("<Button-1>", lambda e: self.on_click(e, True))
            self._center_image(self.original_canvas, self.original_label)
        
        self.processed_label.config(image=image)
        self.processed_label.image = image
        self.processed_label.bind("<Button-1>", lambda e: self.on_click(e, False))
        self._center_image(self.processed_canvas, self.processed_label)
        
        # Mostra original se disponível
        if self.original_image and not is_original:
            self.original_label.config(image=self.original_image)
            self.original_label.image = self.original_image
            self._center_image(self.original_canvas, self.original_label)
    
    def _center_image(self, canvas, label):
        canvas.update_idletasks()
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        
        if hasattr(label, 'image') and label.image:
            img_width = label.image.width()
            img_height = label.image.height()
            
            x = max(0, (canvas_width - img_width) // 2)
            y = max(0, (canvas_height - img_height) // 2)
            
            canvas.coords(canvas.find_all()[0], x, y)
    
    def on_click(self, event, is_original):
        if hasattr(self, 'controller'):
            self.controller.show_pixel_info(event.x, event.y, is_original)
    
    def set_controller(self, controller):
        self.controller = controller
