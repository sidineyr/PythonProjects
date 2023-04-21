import sdl2
import sdl2.ext
import mido

# Inicializa a SDL2
sdl2.ext.init()

# Configuração das notas musicais e seus acidentes
notas_musicais = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
acidentes = ["", "#", "b"]

# Função para reproduzir o som da nota correspondente
def tocar_nota(nota):
    print("Tocando nota:", nota)
    output = mido.open_output('Nome do dispositivo de saída MIDI')  # Substitua pelo nome correto do dispositivo de saída MIDI
    # Lógica para enviar mensagem MIDI para reproduzir a nota correspondente
    # Exemplo de como enviar uma mensagem de nota ligada (note_on) com a nota e a velocidade desejada
    output.send(mido.Message('note_on', note=nota, volume=64))

# Função para lidar com eventos de botão
def handle_button_events(event, buttons):
    if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
        for button in buttons:
            if button.has_point(event.button.x, event.button.y):
                # Obtém a nota do botão pressionado
                nota = button.userdata["nota"]
                # Chama a função para reproduzir o som da nota correspondente
                tocar_nota(nota)

# Cria uma janela de 800x600 pixels
window = sdl2.ext.Window("Teclado Musical com PySDL2", size=(800, 600))
window.show()

# Cria uma lista de botões para as notas e acidentes
buttons = []
for i, nota in enumerate(notas_musicais):
    # Cria um botão para a nota
    nota_button = sdl2.ext.UIButton(label=nota, size=(50, 50), position=(100 + i * 60, 300), bgcolor=(255, 255, 255))
    nota_button.userdata["nota"] = nota
    buttons.append(nota_button)

    for j, acidente in enumerate(acidentes):
        # Cria um botão para o acidente
        acidente_button = sdl2.ext.UIButton(label=acidente, size=(30, 30), position=(130 + i * 60 + j * 30, 270), bgcolor=(200, 200, 200))
        acidente_button.userdata["nota"] = nota + acidente
        buttons.append(acidente_button)

        for button in buttons:
                if button.has_point(event.button.x, event.button.y):
                nota = button.userdata["nota"]
                if event.type == sdl2.SDL_MOUSEBUTTONDOWN:
                tocar_nota(nota)
                elif event.type == sdl2.SDL_MOUSEBUTTONUP:
                print("Parando de tocar nota:", nota)
                output = mido.open_output('Nome do dispositivo de saída MIDI')  # Substitua pelo nome correto do dispositivo de saída MIDI
                # Lógica para enviar mensagem MIDI para desligar a nota correspondente
                # Exemplo de como enviar uma mensagem de nota desligada (note_off)
                output.send(mido.Message('note_off', note=nota, velocity=0))

# Loop principal
running = True
while running:
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False
            break
        # Chama a função de lidar com eventos de botão
        handle_button_events(event, buttons)

# Limpa a memória e finaliza a SDL2
sdl2.ext.qui
