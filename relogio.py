import pygame
import math
import sys
from datetime import datetime

# Inicializar o Pygame
pygame.init()

# Configurações da janela
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Relógio Analógico")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Função para converter ângulo em radianos
def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

# Loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obter a hora atual do computador local
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_second = now.second

    # Limpar a tela
    screen.fill(WHITE)

    # Desenhar o círculo do relógio
    pygame.draw.circle(screen, BLACK, (screen_width // 2, screen_height // 2), 150, 2)

    # Desenhar os ponteiros do relógio
    hour_angle = degrees_to_radians((current_hour % 12) * 30 - 90)
    hour_hand_length = 100
    hour_x = screen_width // 2 + hour_hand_length * math.cos(hour_angle)
    hour_y = screen_height // 2 + hour_hand_length * math.sin(hour_angle)
    pygame.draw.line(screen, BLACK, (screen_width // 2, screen_height // 2), (hour_x, hour_y), 6)

    minute_angle = degrees_to_radians(current_minute * 6 - 90)
    minute_hand_length = 140
    minute_x = screen_width // 2 + minute_hand_length * math.cos(minute_angle)
    minute_y = screen_height // 2 + minute_hand_length * math.sin(minute_angle)
    pygame.draw.line(screen, BLACK, (screen_width // 2, screen_height // 2), (minute_x, minute_y), 4)

    second_angle = degrees_to_radians(current_second * 6 - 90)
    second_hand_length = 160
    second_x = screen_width // 2 + second_hand_length * math.cos(second_angle)
    second_y = screen_height // 2 + second_hand_length * math.sin(second_angle)
    pygame.draw.line(screen, BLACK, (screen_width // 2, screen_height // 2), (second_x, second_y), 2)

    # Atualizar a tela
    pygame.display.flip()

    # Limitar a taxa de quadros
    pygame.time.Clock().tick(60)
