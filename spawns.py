from busc_pos import encontrar_posicao
from exibMapa import mapa

# Geração de pontos no mapa
def spawn_pontos():
    for pos_x in range(len(mapa) - 1):
        for pos_y in range(len(mapa[1]) - 1):
            if mapa[pos_x, pos_y] == ' ':
                mapa[pos_x, pos_y] = '.'
                
# Função para gerar o jogador
def spawn_player():
    if encontrar_posicao('c') == None:
      pos_x = 11
      pos_y = 20
      if mapa[pos_x, pos_y] == ' ':
          mapa[pos_x, pos_y] = 'c'
                
# Função para gerar os inimigos
def spawn_inimigo():
    for i in range(3):
        if encontrar_posicao('①') == None:
            pos_x = 5
            pos_y = 8
            if mapa[pos_x, pos_y] == ' ':
                mapa[pos_x, pos_y] = '①'
                
        if encontrar_posicao('②') == None:
            pos_x = 5
            pos_y = 10
            if mapa[pos_x, pos_y] == ' ':
                mapa[pos_x, pos_y] = '②'
                
        if encontrar_posicao('③') == None:
            pos_x = 5
            pos_y = 13
            if mapa[pos_x, pos_y] == ' ':
                mapa[pos_x, pos_y] = '③'
                