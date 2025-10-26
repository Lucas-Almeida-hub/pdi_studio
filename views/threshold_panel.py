import tkinter as tk
from tkinter import ttk

class ThresholdPanel:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#333")
        
        # Título
        tk.Label(self.frame, text="Controles de Limiarização", bg="#333", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
        
        # Limiarização Global
        global_frame = tk.LabelFrame(self.frame, text="Global", bg="#333", fg="white")
        global_frame.pack(fill="x", padx=5, pady=5)
        
        tk.Label(global_frame, text="Valor:", bg="#333", fg="white").pack(side="left")
        self.threshold_var = tk.IntVar(value=127)
        self.threshold_scale = tk.Scale(global_frame, from_=0, to=255, orient="horizontal", 
                                      variable=self.threshold_var, bg="#333", fg="white")
        self.threshold_scale.pack(side="left", fill="x", expand=True, padx=5)
        
        self.global_btn = tk.Button(global_frame, text="Aplicar Global", bg="#555", fg="white")
        self.global_btn.pack(side="right", padx=5)
        
        # Multissegmentada
        multi_frame = tk.LabelFrame(self.frame, text="Multissegmentada", bg="#333", fg="white")
        multi_frame.pack(fill="x", padx=5, pady=5)
        
        tk.Label(multi_frame, text="Níveis:", bg="#333", fg="white").pack(side="left")
        self.levels_var = tk.IntVar(value=2)
        levels_combo = ttk.Combobox(multi_frame, textvariable=self.levels_var, values=[2, 4, 8, 16], 
                                   state="readonly", width=5)
        levels_combo.pack(side="left", padx=5)
        
        self.multi_btn = tk.Button(multi_frame, text="Aplicar Multi", bg="#555", fg="white")
        self.multi_btn.pack(side="right", padx=5)
        
        # Adaptativa
        adaptive_frame = tk.LabelFrame(self.frame, text="Adaptativa", bg="#333", fg="white")
        adaptive_frame.pack(fill="x", padx=5, pady=5)
        
        tk.Label(adaptive_frame, text="Método:", bg="#333", fg="white").pack(side="left")
        self.method_var = tk.StringVar(value="mean")
        method_combo = ttk.Combobox(adaptive_frame, textvariable=self.method_var, 
                                   values=["mean", "gaussian"], state="readonly", width=8)
        method_combo.pack(side="left", padx=5)
        
        self.adaptive_btn = tk.Button(adaptive_frame, text="Aplicar Adaptativa", bg="#555", fg="white")
        self.adaptive_btn.pack(side="right", padx=5)
        
        # Otsu
        otsu_frame = tk.LabelFrame(self.frame, text="Otsu (Automático)", bg="#333", fg="white")
        otsu_frame.pack(fill="x", padx=5, pady=5)
        
        self.otsu_btn = tk.Button(otsu_frame, text="Aplicar Otsu", bg="#555", fg="white")
        self.otsu_btn.pack(pady=5)
        
        self.otsu_value_label = tk.Label(otsu_frame, text="Valor calculado: -", bg="#333", fg="white")
        self.otsu_value_label.pack()
    
    def set_callbacks(self, global_cb, multi_cb, adaptive_cb, otsu_cb):
        self.global_btn.config(command=global_cb)
        self.multi_btn.config(command=multi_cb)
        self.adaptive_btn.config(command=adaptive_cb)
        self.otsu_btn.config(command=otsu_cb)
    
    def update_otsu_value(self, value):
        self.otsu_value_label.config(text=f"Valor calculado: {value:.1f}")