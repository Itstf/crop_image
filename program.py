# pip install pillow
from PIL import Image

# imagem original
img = Image.open(r'dog.jpg') #imagem de exemplo, pode alterar

esquerda, cima, direita, baixo = (200,20,600,650) # coordenada para cortar
img_cortada = img.crop((esquerda, cima, direita, baixo)) # cortar a imagem
img_cortada.show() # mostrar resultado
