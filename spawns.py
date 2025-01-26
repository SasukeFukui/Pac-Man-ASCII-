from busc_pos import encontrar_posicao
import random
from exibMapa import mapa

# Geração de pontos no mapa
def spawn_pontos():
    for pos_x in range(len(mapa) - 1):
        for pos_y in range(len(mapa[1]) - 1):
            if mapa[pos_x, pos_y] == ' ':
                mapa[pos_x, pos_y] = '.'

# Função para gerar o jogador em uma posição válida
def spawn_player():
    if encontrar_posicao('c') == None:
        while True:
            pos_x = random.randint(1, len(mapa) - 1)
            pos_y = random.randint(1, len(mapa[1]) - 1)
            if mapa[pos_x, pos_y] == ' ':
                mapa[pos_x, pos_y] = 'c'
                break