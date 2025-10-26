import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class HistogramCanvas:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)
        
        # Configuração do matplotlib
        plt.style.use('dark_background')
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(10, 4))
        self.fig.patch.set_facecolor('#222222')
        
        # Canvas do matplotlib
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        # Controles de brilho e contraste
        controls_frame = tk.Frame(self.frame, bg="#333")
        controls_frame.pack(fill="x", pady=5)
        
        # Brilho
        tk.Label(controls_frame, text="Brilho:", bg="#333", fg="white").pack(side="left")
        self.brightness_var = tk.IntVar(value=0)
        self.brightness_scale = tk.Scale(controls_frame, from_=-100, to=100, 
                                       orient="horizontal", variable=self.brightness_var,
                                       bg="#333", fg="white", highlightthickness=0)
        self.brightness_scale.pack(side="left", padx=5)
        
        # Contraste
        tk.Label(controls_frame, text="Contraste:", bg="#333", fg="white").pack(side="left")
        self.contrast_var = tk.DoubleVar(value=1.0)
        self.contrast_scale = tk.Scale(controls_frame, from_=0.1, to=3.0, resolution=0.1,
                                     orient="horizontal", variable=self.contrast_var,
                                     bg="#333", fg="white", highlightthickness=0)
        self.contrast_scale.pack(side="left", padx=5)
        
        # Botão aplicar
        self.apply_btn = tk.Button(controls_frame, text="Aplicar", bg="#555", fg="white")
        self.apply_btn.pack(side="left", padx=10)
    
    def plot_histograms(self, hist_original, hist_processed=None):
        self.ax1.clear()
        self.ax2.clear()
        
        if hist_original:
            hist_b, hist_g, hist_r = hist_original
            x = np.arange(256)
            
            self.ax1.plot(x, hist_b, color='blue', alpha=0.7, label='Blue')
            self.ax1.plot(x, hist_g, color='green', alpha=0.7, label='Green') 
            self.ax1.plot(x, hist_r, color='red', alpha=0.7, label='Red')
            self.ax1.set_title('Histograma Original', color='white')
            self.ax1.legend()
        
        if hist_processed:
            hist_b, hist_g, hist_r = hist_processed
            x = np.arange(256)
            
            self.ax2.plot(x, hist_b, color='blue', alpha=0.7, label='Blue')
            self.ax2.plot(x, hist_g, color='green', alpha=0.7, label='Green')
            self.ax2.plot(x, hist_r, color='red', alpha=0.7, label='Red')
            self.ax2.set_title('Histograma Processado', color='white')
            self.ax2.legend()
        
        self.canvas.draw()
    
    def set_apply_callback(self, callback):
        self.apply_btn.config(command=callback)