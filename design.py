from PIL import Image, ImageDraw, ImageFilter

# Dimensões da imagem
largura = 300
altura = 300

# Crie uma nova imagem em branco com canal alfa (transparência)
imagem = Image.new("RGBA", (largura, altura), (255, 255, 255, 0))
desenho = ImageDraw.Draw(imagem)

# Cores
cor_parafuso = (169, 169, 169, 255)  # Cor cinza com canal alfa 255 (sem transparência)
cor_sombra = (105, 105, 105, 128)    # Cor cinza mais escura com canal alfa 128 (transparência)

# Desenhe o corpo do parafuso
desenho.rectangle((100, 50, 200, 250), fill=cor_parafuso)

# Desenhe a cabeça do parafuso
desenho.ellipse((125, 25, 175, 75), fill=cor_parafuso)

# Crie um efeito de sombreamento para dar a ilusão de 3D
sombra = Image.new("RGBA", (largura, altura), (0, 0, 0, 0))  # Máscara de sombra transparente
sombra_desenho = ImageDraw.Draw(sombra)
sombra_desenho.ellipse((125, 75, 175, 125), fill=cor_sombra)

# Coloque a sombra na imagem principal
imagem = Image.alpha_composite(imagem, sombra)

# Salve a imagem
imagem.save("parafuso.png")

# Exiba a imagem
imagem.show()
