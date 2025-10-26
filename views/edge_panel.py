import tkinter as tk

class EdgePanel:
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bg="#333")
        
        tk.Label(self.frame, text="Detecção de Bordas", bg="#333", fg="white", font=("Arial", 12, "bold")).pack(pady=5)
        
        # Canny
        canny_frame = tk.LabelFrame(self.frame, text="Canny", bg="#333", fg="white")
        canny_frame.pack(fill="x", padx=5, pady=5)
        
        tk.Label(canny_frame, text="Min:", bg="#333", fg="white").pack(side="left")
        self.canny_low = tk.IntVar(value=50)
        tk.Scale(canny_frame, from_=0, to=255, orient="horizontal", variable=self.canny_low, bg="#333", fg="white").pack(side="left", fill="x", expand=True)
        
        tk.Label(canny_frame, text="Max:", bg="#333", fg="white").pack(side="left")
        self.canny_high = tk.IntVar(value=150)
        tk.Scale(canny_frame, from_=0, to=255, orient="horizontal", variable=self.canny_high, bg="#333", fg="white").pack(side="left", fill="x", expand=True)
        
        self.canny_btn = tk.Button(canny_frame, text="Aplicar Canny", bg="#555", fg="white")
        self.canny_btn.pack(side="right", padx=5)
        
        # Sobel
        sobel_frame = tk.LabelFrame(self.frame, text="Sobel", bg="#333", fg="white")
        sobel_frame.pack(fill="x", padx=5, pady=5)
        
        self.sobel_btn = tk.Button(sobel_frame, text="Aplicar Sobel", bg="#555", fg="white")
        self.sobel_btn.pack(pady=5)
        
        # Laplaciano
        laplacian_frame = tk.LabelFrame(self.frame, text="Laplaciano", bg="#333", fg="white")
        laplacian_frame.pack(fill="x", padx=5, pady=5)
        
        self.laplacian_btn = tk.Button(laplacian_frame, text="Aplicar Laplaciano", bg="#555", fg="white")
        self.laplacian_btn.pack(pady=5)
    
    def set_callbacks(self, canny_cb, sobel_cb, laplacian_cb):
        self.canny_btn.config(command=canny_cb)
        self.sobel_btn.config(command=sobel_cb)
        self.laplacian_btn.config(command=laplacian_cb)