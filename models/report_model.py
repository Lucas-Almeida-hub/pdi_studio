from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import matplotlib.pyplot as plt
import cv2
import numpy as np
from datetime import datetime
import os
import tempfile

class ReportModel:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self.title_style = ParagraphStyle('CustomTitle', parent=self.styles['Heading1'], 
                                        fontSize=18, spaceAfter=30, alignment=1)
    
    def generate_report(self, original_image, processed_image, operations_log, output_path):
        doc = SimpleDocTemplate(output_path, pagesize=A4)
        story = []
        
        # Título
        title = Paragraph("Relatório de Processamento de Imagens", self.title_style)
        story.append(title)
        story.append(Spacer(1, 20))
        
        # Data
        date_text = f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        story.append(Paragraph(date_text, self.styles['Normal']))
        story.append(Spacer(1, 20))
        
        # Salvar imagens temporárias
        temp_dir = tempfile.mkdtemp()
        original_path = os.path.join(temp_dir, 'original.png')
        processed_path = os.path.join(temp_dir, 'processed.png')
        
        # Garantir que as imagens sejam salvas corretamente
        success_orig = cv2.imwrite(original_path, original_image)
        success_proc = cv2.imwrite(processed_path, processed_image)
        
        if not success_orig or not success_proc:
            raise Exception("Erro ao salvar imagens temporárias")
        
        # Adicionar imagens
        story.append(Paragraph("Imagem Original:", self.styles['Heading2']))
        story.append(Image(original_path, width=3*inch, height=2*inch))
        story.append(Spacer(1, 10))
        
        story.append(Paragraph("Imagem Processada:", self.styles['Heading2']))
        story.append(Image(processed_path, width=3*inch, height=2*inch))
        story.append(Spacer(1, 20))
        
        # Log de operações
        story.append(Paragraph("Operações Realizadas:", self.styles['Heading2']))
        if operations_log:
            for operation in operations_log:
                story.append(Paragraph(f"• {operation}", self.styles['Normal']))
        else:
            story.append(Paragraph("• Nenhuma operação realizada", self.styles['Normal']))
        
        doc.build(story)
        
        # Limpar arquivos temporários
        try:
            os.remove(original_path)
            os.remove(processed_path)
            os.rmdir(temp_dir)
        except:
            pass  # Ignora erros de limpeza