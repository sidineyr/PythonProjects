import pygame
import math
import random

# Define as formas a serem usadas no caleidoscópio
shapes = ["circle", "star", "square"]

# Define as cores a serem usadas no caleidoscópio
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Define o tamanho da janela
width = 800
height = 600

# Inicializa o pygame
pygame.init()

# Cria a janela
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Caleidoscópio")

# Define o centro da janela
center = (width // 2, height // 2)

# Define a velocidade de rotação das formas
rotation_speed = 0.05

# Define a quantidade de formas a serem desenhadas
shape_count = 36

# Define o tamanho das formas
shape_size = 200

# Loop principal do jogo
running = True
while running:
    # Trata os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Preenche o fundo da janela com a cor branca
    screen.fill((255, 255, 255))

    # Desenha as formas
    for i in range(shape_count):
        # Escolhe uma forma aleatória
        shape = random.choice(shapes)

        # Calcula a posição da forma na circunferência
        angle = 2 * math.pi * i / shape_count
        x = int(center[0] + shape_size * math.cos(angle))
        y = int(center[1] + shape_size * math.sin(angle))

        # Calcula a rotação da forma
        rotation = angle + pygame.time.get_ticks() * rotation_speed

        # Desenha a forma
        if shape == "circle":
            pygame.draw.circle(screen, colors[i % len(colors)], (x, y), shape_size//2)
        elif shape == "star":
            points = [(x + shape_size * math.cos(rotation + angle), y + shape_size * math.sin(rotation + angle)) if i % 2 == 0
                      else (x + shape_size/2 * math.cos(rotation + angle), y + shape_size/2 * math.sin(rotation + angle)) for i, angle in enumerate([0, math.pi/5, 2*math.pi*2/5, math.pi*3/5, math.pi*4/5, math.pi, math.pi*6/5, math.pi*7/5, math.pi*8/5, math.pi*9/5])]
            pygame.draw.polygon(screen, colors[i % len(colors)], points)
        elif shape == "square":
            points = [(x + shape_size/2 * math.cos(rotation + angle), y + shape_size/2 * math.sin(rotation + angle)) for angle in [0, math.pi/2, math.pi, math.pi*3/2]]
            pygame.draw.polygon(screen, colors[i % len(colors)], points)

    # Atualiza a janela
    pygame.display.flip()

# Finaliza o pygame
pygame.quit()
