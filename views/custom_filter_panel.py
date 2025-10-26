import tkinter as tk
from tkinter import ttk
import numpy as np

class CustomFilterPanel:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#333")
        
        tk.Label(self.frame, text="Filtros Customizados", bg="#333", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
        
        # Kernel 3x3
        kernel_frame = tk.LabelFrame(self.frame, text="Kernel 3x3", bg="#333", fg="white")
        kernel_frame.pack(fill="x", padx=5, pady=5)
        
        self.kernel_entries = []
        for i in range(3):
            row_frame = tk.Frame(kernel_frame, bg="#333")
            row_frame.pack()
            row_entries = []
            for j in range(3):
                entry = tk.Entry(row_frame, width=5, justify="center")
                entry.pack(side="left", padx=2, pady=2)
                entry.insert(0, "0")
                row_entries.append(entry)
            self.kernel_entries.append(row_entries)
        
        # Presets
        presets_frame = tk.Frame(kernel_frame, bg="#333")
        presets_frame.pack(fill="x", pady=5)
        
        tk.Button(presets_frame, text="Blur", command=self.set_blur, bg="#555", fg="white").pack(side="left", padx=2)
        tk.Button(presets_frame, text="Sharpen", command=self.set_sharpen, bg="#555", fg="white").pack(side="left", padx=2)
        tk.Button(presets_frame, text="Edge", command=self.set_edge, bg="#555", fg="white").pack(side="left", padx=2)
        tk.Button(presets_frame, text="Emboss", command=self.set_emboss, bg="#555", fg="white").pack(side="left", padx=2)
        
        self.apply_btn = tk.Button(kernel_frame, text="Aplicar Filtro", bg="#555", fg="white")
        self.apply_btn.pack(pady=5)
    
    def set_blur(self):
        kernel = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self._set_kernel(kernel)
    
    def set_sharpen(self):
        kernel = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
        self._set_kernel(kernel)
    
    def set_edge(self):
        kernel = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
        self._set_kernel(kernel)
    
    def set_emboss(self):
        kernel = [[-2, -1, 0], [-1, 1, 1], [0, 1, 2]]
        self._set_kernel(kernel)
    
    def _set_kernel(self, kernel):
        for i in range(3):
            for j in range(3):
                self.kernel_entries[i][j].delete(0, tk.END)
                self.kernel_entries[i][j].insert(0, str(kernel[i][j]))
    
    def get_kernel(self):
        kernel = []
        for i in range(3):
            row = []
            for j in range(3):
                try:
                    value = float(self.kernel_entries[i][j].get())
                    row.append(value)
                except:
                    row.append(0)
            kernel.append(row)
        return np.array(kernel, dtype=np.float32)
    
    def set_callback(self, callback):
        self.apply_btn.config(command=callback)