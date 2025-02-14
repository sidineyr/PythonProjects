import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import Tuple

# Constantes (hardcoded)
G = 6.67430e-11  # Constante gravitacional (m^3 kg^-1 s^-2)
M_sol = 1.989e30  # Massa do Sol (kg)
M_terra = 5.972e24  # Massa da Terra (kg)
R_terra = 6.371e6  # Raio da Terra (m)
AU = 1.496e11  # Unidade Astronômica (m)

# Função para calcular a velocidade de escape
def velocidade_escape(massa_planeta: float, raio_planeta: float) -> float:
    return np.sqrt(2 * G * massa_planeta / raio_planeta)

# Função para calcular a trajetória orbital
def calcular_trajetoria_orbital(v0: float, angulo: float, tempo_total: float, dt: float) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # Posição inicial (Terra)
    x0 = AU  # Distância da Terra ao Sol
    y0 = 0

    # Velocidade inicial (em relação ao Sol)
    vx0 = -v0 * np.sin(angulo)  # Componente x da velocidade
    vy0 = v0 * np.cos(angulo)   # Componente y da velocidade

    # Arrays para armazenar a trajetória
    tempo = np.arange(0, tempo_total, dt)
    x = np.zeros_like(tempo)
    y = np.zeros_like(tempo)
    x[0], y[0] = x0, y0

    # Simulação da trajetória orbital
    for i in range(1, len(tempo)):
        # Calcula a distância ao Sol
        r_squared = x[i-1]**2 + y[i-1]**2
        if r_squared <= 0:  # Evita valores negativos ou zero
            break
        r = np.sqrt(r_squared)

        # Verifica se a distância é válida
        if np.isnan(r) or np.isinf(r):
            break

        # Calcula a aceleração gravitacional
        ax = -G * M_sol * x[i-1] / r**3  # Aceleração gravitacional (x)
        ay = -G * M_sol * y[i-1] / r**3  # Aceleração gravitacional (y)

        # Atualiza a velocidade e a posição
        vx0 += ax * dt
        vy0 += ay * dt
        x[i] = x[i-1] + vx0 * dt
        y[i] = y[i-1] + vy0 * dt

        # Verifica se o objeto colidiu com o Sol
        if colisao_com_sol(np.array([x[i]]), np.array([y[i]])):
            break

    return tempo[:i], x[:i], y[:i]

# Função para verificar colisão com o Sol
def colisao_com_sol(x: np.ndarray, y: np.ndarray, raio_sol: float = 6.957e8) -> bool:
    distancia_objeto_sol = np.sqrt(x**2 + y**2)
    return np.any(distancia_objeto_sol <= raio_sol)

# Função principal para executar a simulação
def main():
    # Parâmetros iniciais
    v0 = velocidade_escape(M_terra, R_terra)  # Velocidade de escape da Terra
    angulo = np.radians(45)  # Ângulo de lançamento (45 graus)
    tempo_total = 365 * 24 * 60 * 60  # 1 ano em segundos
    dt = 1000  # Passo de tempo (s)

    # Simulação da trajetória orbital
    tempo, x, y = calcular_trajetoria_orbital(v0, angulo, tempo_total, dt)

    # Conversão de unidades
    tempo_dias = tempo / (60 * 60 * 24)  # Converter tempo de segundos para dias
    distancia_km = np.sqrt(x**2 + y**2) / 1e3  # Converter distância de metros para quilômetros

    # Configuração da animação
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_facecolor('black')  # Fundo preto
    ax.set_xlabel("Tempo (dias)")
    ax.set_ylabel("Distância do Sol (km)")
    ax.set_title("Trajetória Orbital de um Objeto Lançado ao Espaço")
    ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
    ax.set_xlim(0, max(tempo_dias))
    ax.set_ylim(0, max(distancia_km) * 1.1)

    # Linha da trajetória
    linha, = ax.plot([], [], color='white', linestyle='-', linewidth=1, label="Trajetória")
    ponto, = ax.plot([], [], 'o', color='yellow', markersize=5, label="Objeto")

    # Função de inicialização da animação
    def init():
        linha.set_data([], [])
        ponto.set_data([], [])
        return linha, ponto

    # Função de atualização da animação
    def update(frame):
        linha.set_data(tempo_dias[:frame], distancia_km[:frame])
        ponto.set_data(tempo_dias[frame], distancia_km[frame])
        return linha, ponto

    # Criar a animação
    frames = len(tempo_dias)
    anim = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50)

    # Exibir a animação
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
