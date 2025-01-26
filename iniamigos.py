from busc_pos import encontrar_posicao
import numpy as np
import random
from exibMapa import mapa,exibir_mapa

caractere_antigo = [' ',' ',' ']

def perseguir_player(caractere):
    def perseguindo(posição_fantasma, posição_player):
        sla = random.randint(0, 2)
        if sla != 0:
            if posição_fantasma[0] > posição_player[0]:
                return 'w' 
            if posição_fantasma[0] < posição_player[0]:    
                return 's' 
            if posição_fantasma[1] > posição_player[1]:
                return 'a' 
            if posição_fantasma[1] < posição_player[1]:    
                return 'd' 
        else:
            return random.choice(['w', 's', 'a', 'd'])

    posição_fantasma = encontrar_posicao(caractere)
    posição_player = encontrar_posicao('c')
    if posição_fantasma and posição_player:
        if posição_fantasma[0] == posição_player[0] or posição_player[1] == posição_fantasma[1]:
            return perseguindo(posição_fantasma, posição_player)
    return random.choice(['w', 's', 'a', 'd'])

# Função para movimento dos inimigos
def mover_inimigos():
    global caractere_antigo

    ninimigos = ['①','②','③']
    for i in range(len(ninimigos)):
        inimigos = np.argwhere(mapa == ninimigos[i])
  
        for inimigo in inimigos:    
            pos_x, pos_y = inimigo
            nova_pos_x, nova_pos_y = pos_x, pos_y
            direcao = perseguir_player(ninimigos[i])

            match direcao:
                case 'w':
                    nova_pos_x -= 1
                case 's':
                    nova_pos_x += 1
                case 'a':
                    nova_pos_y -= 1
                case 'd':
                    nova_pos_y += 1

            prox_caractere = mapa[nova_pos_x, nova_pos_y]

            match prox_caractere:
                case ' ':
                    mapa[pos_x, pos_y] = caractere_antigo[i]
                    mapa[nova_pos_x, nova_pos_y] = ninimigos[i]
                    caractere_antigo[i] = ' '
                
                case '.':
                    mapa[pos_x, pos_y] = caractere_antigo[i]
                    mapa[nova_pos_x, nova_pos_y] = ninimigos[i]
                    caractere_antigo[i] = '.'

                case 'c':
                    mapa[pos_x, pos_y] = caractere_antigo[i]
                    mapa[nova_pos_x, nova_pos_y] = ninimigos[i]
                    exibir_mapa()
                    print("Seu Pac-Man foi comido! FIM DE JOGO")
                    return True