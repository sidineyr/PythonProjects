import pygame
import pygame.midi
import mido

# Inicializar o Pygame
pygame.init()
pygame.midi.init()

# Configurações da janela
screen_width = 800
screen_height = 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Teclado MIDI virtual")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Configurações das teclas
key_width = screen_width // 12
key_height = screen_height // 2
key_colors = [WHITE, BLACK, WHITE, BLACK, WHITE, WHITE, BLACK, WHITE, BLACK, WHITE, BLACK, WHITE]
key_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Inicializar o player de MIDI
midi_out = None
try:
    midi_out = mido.open_output()
except:
    print("Nenhum player de MIDI encontrado no sistema.")

# Loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.midi.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode in key_notes:
                note = key_notes.index(event.unicode)
                print(f"Nota: {event.unicode} ({note + 60})")  # Imprime a nota correspondente
                if midi_out is not None:
                    # Enviar o sinal MIDI para o player de MIDI
                    midi_out.send(mido.Message('note_on', note=note + 60, velocity=64))
        elif event.type == pygame.KEYUP:
            if event.unicode in key_notes:
                note = key_notes.index(event.unicode)
                if midi_out is not None:
                    # Enviar o sinal de parar de tocar a nota MIDI
                    midi_out.send(mido.Message('note_off', note=note + 60, velocity=64))

    # Limpar a tela
    screen.fill(WHITE)

    # Desenhar as teclas
    for i in range(12):
        key_x = i * key_width
        key_rect = pygame.Rect(key_x, 0, key_width, key_height)
        pygame.draw.rect(screen, key_colors[i], key_rect)

        # Desenhar o nome da nota na tecla
        note_font = pygame.font.Font(None, 36)
        note_text = note_font.render(key_notes[i], True, BLACK)
        screen.blit(note_text, (key_x + key_width // 2 - note_text.get_width() // 2, key_height // 2 - note_text.get_height() // 2))

    # Atualizar a tela
    pygame.display.flip()

# Fechar o Pygame
pygame.quit()
pygame.midi.quit()
