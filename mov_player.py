from busc_pos import encontrar_posicao
from exibMapa import mapa,exibir_mapa
from cont_pontuacao import conta_ponto
import guardando as g
import inicio 
import time

#funcao para mover o jogador
def mover_jogador(direcao):
    pos_x, pos_y = encontrar_posicao('c')
    nova_pos_x, nova_pos_y = pos_x, pos_y

    if direcao == 'w':  
        nova_pos_x -= 1
    elif direcao == 's': 
        nova_pos_x += 1
    elif direcao == 'a':  
        nova_pos_y -= 1
    elif direcao == 'd':  
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
                g.score_guardado('score.bin','venceu')
                time.sleep(0.9)
                mapa[nova_pos_x, nova_pos_y] = ' '
                inimigos = ['①','②','③']
                for i in range(len(inimigos)):
                    pos_x,pos_y = encontrar_posicao(inimigos[i])
                    mapa[pos_x, pos_y] = ' '
                
                inicio.main()
