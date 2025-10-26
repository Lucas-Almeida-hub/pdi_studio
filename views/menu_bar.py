import tkinter as tk

class MenuBar:
    def __init__(self, root, controller):
        self.controller = controller
        self.menubar = tk.Menu(root)

        # Menu Arquivo
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Abrir", command=controller.open_image)
        file_menu.add_command(label="Salvar como...", command=controller.save_image)
        file_menu.add_command(label="Reset", command=controller.reset_image)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=root.quit)
        self.menubar.add_cascade(label="Arquivo", menu=file_menu)

        # Menu Filtros
        filter_menu = tk.Menu(self.menubar, tearoff=0)
        filter_menu.add_command(label="Converter para tons de cinza", command=controller.apply_gray)
        filter_menu.add_command(label="Equalizar histograma", command=controller.apply_equalization)
        self.menubar.add_cascade(label="Filtros", menu=filter_menu)

        # Menu Conversões
        convert_menu = tk.Menu(self.menubar, tearoff=0)
        convert_menu.add_command(label="RGBA", command=controller.convert_rgba)
        convert_menu.add_command(label="HSV", command=controller.convert_hsv)
        convert_menu.add_command(label="LAB", command=controller.convert_lab)
        convert_menu.add_command(label="CMYK", command=controller.convert_cmyk)
        self.menubar.add_cascade(label="Conversões", menu=convert_menu)
        
        # Menu Histograma
        hist_menu = tk.Menu(self.menubar, tearoff=0)
        hist_menu.add_command(label="Abrir Análise", command=controller.open_histogram)
        hist_menu.add_command(label="Equalizar Automático", command=controller.apply_equalization)
        self.menubar.add_cascade(label="Histograma", menu=hist_menu)
        
        # Menu Limiarização
        threshold_menu = tk.Menu(self.menubar, tearoff=0)
        threshold_menu.add_command(label="Abrir Controles", command=controller.open_threshold)
        self.menubar.add_cascade(label="Limiarização", menu=threshold_menu)
        
        # Menu Bordas
        edge_menu = tk.Menu(self.menubar, tearoff=0)
        edge_menu.add_command(label="Abrir Controles", command=controller.open_edges)
        self.menubar.add_cascade(label="Bordas", menu=edge_menu)
        
        # Menu Filtros Customizados
        custom_menu = tk.Menu(self.menubar, tearoff=0)
        custom_menu.add_command(label="Abrir Editor", command=controller.open_custom_filter)
        self.menubar.add_cascade(label="Filtros Custom", menu=custom_menu)
        
        # Menu Relatório
        report_menu = tk.Menu(self.menubar, tearoff=0)
        report_menu.add_command(label="Gerar PDF", command=controller.generate_report)
        self.menubar.add_cascade(label="Relatório", menu=report_menu)
