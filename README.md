# 🖼️ PDI Studio - Sistema Interativo de Processamento de Imagens

Sistema completo de processamento digital de imagens desenvolvido em Python com interface gráfica Tkinter, ideal para estudos acadêmicos e aplicações profissionais.

## 🚀 Funcionalidades

### 📁 **Gerenciamento de Imagens**
- ✅ Abertura e salvamento em múltiplos formatos (.jpg, .png, .bmp)
- ✅ Visualização lado a lado (original vs processada)
- ✅ Reset para estado inicial
- ✅ Informações de pixel (valores RGB) por clique

### 🎨 **Processamento Básico**
- ✅ Conversão para tons de cinza
- ✅ Equalização de histograma automática
- ✅ Ajuste manual de brilho e contraste

### 🌈 **Conversões de Espaço de Cor**
- ✅ RGB ↔ RGBA
- ✅ RGB ↔ HSV  
- ✅ RGB ↔ LAB
- ✅ RGB ↔ CMYK
- ✅ RGB ↔ L (tons de cinza)

### 📊 **Análise de Histograma**
- ✅ Exibição de histogramas RGB
- ✅ Comparação original vs processada
- ✅ Controles interativos de brilho/contraste
- ✅ Visualização em tempo real

### 🔲 **Limiarização (Thresholding)**
- ✅ **Global**: Valor ajustável por slider
- ✅ **Multissegmentada**: 2, 4, 8 ou 16 níveis
- ✅ **Adaptativa**: Métodos Mean e Gaussian
- ✅ **Otsu**: Cálculo automático do threshold ótimo

### 🔍 **Detecção de Bordas**
- ✅ **Canny**: Controles de threshold mín/máx
- ✅ **Sobel**: Detecção de gradientes
- ✅ **Laplaciano**: Segunda derivada

### 🎛️ **Filtros Customizados**
- ✅ Editor de kernel 3x3 interativo
- ✅ Presets: Blur, Sharpen, Edge, Emboss
- ✅ Aplicação dinâmica em tempo real

### 📄 **Geração de Relatórios**
- ✅ Exportação automática para PDF
- ✅ Imagens original e processada
- ✅ Log completo de operações
- ✅ Data/hora de geração

## 🏗️ Arquitetura

```
pdi_studio/
├── main.py                 # Ponto de entrada
├── controllers/
│   └── controller.py       # Lógica de controle MVC
├── models/
│   ├── model.py           # Model principal
│   ├── histogram_model.py # Análise de histograma
│   ├── threshold_model.py # Limiarização
│   ├── edge_model.py      # Detecção de bordas
│   └── report_model.py    # Geração de relatórios
├── views/
│   ├── view.py            # View principal
│   ├── menu_bar.py        # Barra de menu
│   ├── image_panel.py     # Painel de imagens
│   ├── control_panel.py   # Painel de controle
│   ├── histogram_canvas.py # Canvas de histograma
│   ├── threshold_panel.py  # Controles de limiarização
│   ├── edge_panel.py      # Controles de bordas
│   └── custom_filter_panel.py # Editor de filtros
└── documents/
    └── pdi_studio.odt     # Documentação
```

## 🛠️ Instalação

### Opção 1: Conda (Recomendado)
```bash
# Criar ambiente
conda env create -f environment.yml

# Ativar ambiente
conda activate pdi_studio

# Executar
python main.py
```

### Opção 2: Pip
```bash
# Instalar dependências
pip install opencv-python numpy matplotlib pillow reportlab

# Executar
python main.py
```

## 📋 Dependências

- **Python 3.10+**
- **OpenCV** - Processamento de imagens
- **NumPy** - Operações matemáticas
- **Matplotlib** - Visualização de histogramas
- **Pillow** - Manipulação de imagens
- **ReportLab** - Geração de PDFs
- **Tkinter** - Interface gráfica (incluído no Python)

## 🎯 Como Usar

### 1. **Carregar Imagem**
- Menu `Arquivo` → `Abrir`
- Formatos suportados: PNG, JPG, JPEG, BMP

### 2. **Aplicar Processamentos**
- **Filtros**: Tons de cinza, equalização
- **Conversões**: RGB, HSV, LAB, CMYK
- **Limiarização**: Global, adaptativa, Otsu, multissegmentada
- **Bordas**: Canny, Sobel, Laplaciano
- **Filtros Custom**: Crie seus próprios kernels

### 3. **Analisar Resultados**
- **Histograma**: Menu `Histograma` → `Abrir Análise`
- **Pixel Info**: Clique na imagem para ver valores RGB
- **Comparação**: Visualização lado a lado automática

### 4. **Gerar Relatório**
- Menu `Relatório` → `Gerar PDF`
- Inclui imagens e log completo de operações

## 🎓 Ideal para

- **Trabalhos de Conclusão de Curso (TCC)**
- **Estudos de Processamento Digital de Imagens**
- **Prototipagem rápida de algoritmos**
- **Demonstrações acadêmicas**
- **Análise comparativa de técnicas**

## 🔧 Recursos Técnicos

- **Arquitetura MVC** bem estruturada
- **Interface responsiva** com redimensionamento automático
- **Log completo** de todas as operações
- **Tratamento de erros** robusto
- **Código modular** e extensível

## 📸 Screenshots

### Interface Principal
- Visualização lado a lado das imagens
- Painel de controle com log de operações
- Menu completo com todas as funcionalidades

### Análise de Histograma
- Gráficos RGB interativos
- Controles de brilho e contraste
- Comparação original vs processada

### Editor de Filtros Customizados
- Kernel 3x3 editável
- Presets prontos para uso
- Aplicação em tempo real

## 🤝 Contribuição

Projeto desenvolvido para fins acadêmicos. Sugestões e melhorias são bem-vindas!

## 📄 Licença

Este projeto é de uso acadêmico e educacional.

---

**Desenvolvido com ❤️ para a comunidade acadêmica de Processamento Digital de Imagens**