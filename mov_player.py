from busc_pos import encontrar_posicao
from exibMapa import mapa,exibir_mapa
from cont_pontuacao import conta_ponto
import os


def mover_jogador(direcao):
    pos_x, pos_y = encontrar_posicao('c')
    nova_pos_x, nova_pos_y = pos_x, pos_y

    if direcao == 'w':  # Cima
        nova_pos_x -= 1
    elif direcao == 's':  # Baixo
        nova_pos_x += 1
    elif direcao == 'a':  # Esquerda
        nova_pos_y -= 1
    elif direcao == 'd':  # Direita
        nova_pos_y += 1
    
    prox_caractere = mapa[nova_pos_x, nova_pos_y]

    match prox_caractere:
        case ' ':
            mapa[pos_x, pos_y] = ' '
            mapa[nova_pos_x, nova_pos_y] = 'c'

        case '.':
            mapa[pos_x, pos_y] = ' '
            mapa[nova_pos_x, nova_pos_y] = 'c'
            conta_ponto(1)  
            if encontrar_posicao('.') == None:
                exibir_mapa()
                print("Você ganhou!")
                os._exit(0)
