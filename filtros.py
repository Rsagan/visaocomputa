import cv2
import numpy as np

def aplicar_filtros(imagem_path):
    imagem = cv2.imread(imagem_path)
   
    # A- Blur (desfoque)
    blur = cv2.GaussianBlur(imagem, (15, 15), 0)
    cv2.imwrite("filtro_blur.png", blur)
   
    # B- Detecção de Bordas
    bordas = cv2.Canny(imagem, 100, 200)
    cv2.imwrite("filtro_bordas.png", bordas)
   
    # C- Escala de Cinza
    escala_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("filtro_cinza.png", escala_cinza)
   
    # D- Redimensionamento (50% do tamanho original)
    altura, largura = imagem.shape[:2]
    nova_dimensao = (largura // 2, altura // 2)
    imagem_redimensionada = cv2.resize(imagem, nova_dimensao, interpolation=cv2.INTER_AREA)
    cv2.imwrite("filtro_redimensionado.png", imagem_redimensionada)

def aplicar_overlays(imagem_path):
    imagem = cv2.imread(imagem_path)
    altura, largura = imagem.shape[:2]
   
    # A - Retângulo azul (10px da borda, espessura 2px)
    cv2.rectangle(imagem, (10, 10), (largura - 10, altura - 10), (255, 0, 0), 2)
   
    # B - Círculo vermelho no centro (raio 200px, espessura 1px)
    centro = (largura // 2, altura // 2)
    cv2.circle(imagem, centro, 200, (0, 0, 255), 1)
   
    # C - Círculo verde preenchido no centro (raio 50px)
    cv2.circle(imagem, centro, 50, (0, 255, 0), -1)
   
    # D - Texto
    texto = "Engenharia de Software"
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    tamanho_fonte = 1
    espessura_fonte = 2
    cor_texto = (0, 0, 0)
    margem = 20
    (largura_texto, altura_texto), _ = cv2.getTextSize(texto, fonte, tamanho_fonte, espessura_fonte)
    posicao_texto = (largura - largura_texto - margem, altura - margem)
    cv2.putText(imagem, texto, posicao_texto, fonte, tamanho_fonte, cor_texto, espessura_fonte)
   
    # Salvar imagem com overlays
    cv2.imwrite("imagem_overlays.jpg", imagem)

# Caminho da imagem original (substituir pelo caminho correto)
imagem_path = "gramado.jpg"

# Aplicar filtros e overlays
aplicar_filtros(imagem_path)
aplicar_overlays(imagem_path)
