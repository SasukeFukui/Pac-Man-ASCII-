import random
import os
import time
import numpy as np
import keyboard

# Definir o mapa do jogo como uma matriz numpy
mapa = np.array([
    ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"],
    ["□"," "," "," "," ","□"," "," "," "," "," "," "," "," "," "," ","□"," "," "," "," ","□"],
    ["□"," ","□","□"," ","□"," ","□","□","□","□","□","□","□","□"," ","□"," ","□","□"," ","□"],
    ["□"," ","□"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","□"," ","□"],
    ["□"," ","□"," ","□","□"," ","□"," "," "," "," "," "," ","□"," ","□","□"," ","□"," ","□"],
    ["□"," ","□"," "," "," "," ","□"," "," ","①","②","③"," ","□"," "," "," "," ","□"," ","□"],
    ["□"," "," "," ","□","□"," ","□","□","□","□","□","□","□","□"," ","□","□"," "," "," ","□"],
    ["□"," ","□"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","□"," ","□"],
    ["□"," ","□"," ","□","□"," ","□","□","□","□","□","□","□","□"," ","□","□"," ","□"," ","□"],
    ["□"," ","□"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","□"," ","□"],
    ["□"," ","□","□"," ","□"," ","□","□","□","□","□","□","□","□"," ","□"," ","□","□"," ","□"],
    ["□"," "," "," "," ","□"," "," "," "," "," "," "," "," "," "," ","□"," "," "," ","c","□"],
    ["□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□","□"]
])

pontuacao = 0
caractere_antigo = [' ',' ',' ']

# Função para exibir o mapa
def exibir_mapa():
    os.system('cls' if os.name == 'nt' else 'clear')
    for linha in mapa:
        print("".join(linha))
    print("Sua pontuação: ", pontuacao)

# Função para encontrar a posição de um símbolo no mapa
def encontrar_posicao(simb):
    result = np.where(mapa == simb)
    if result[0].size > 0:
        return result[0][0], result[1][0]
    return None

# Função para mover o jogador
def mover_jogador(direcao):
    pos_x, pos_y = encontrar_posicao('c')
    nova_pos_x, nova_pos_y = pos_x, pos_y
    global pontuacao

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
            pontuacao += 1  
            if encontrar_posicao('.') == None:
                exibir_mapa()
                print("Você ganhou!")
                os._exit(0)

# Função para o fantasma perseguir o jogador
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

# Função principal para rodar o jogo
def jogar():
    spawn_pontos()
    spawn_player()
    exibir_mapa()  
    while True:
        if keyboard.is_pressed('w'):
            mover_jogador('w')
        elif keyboard.is_pressed('s'):
            mover_jogador('s')
        elif keyboard.is_pressed('a'):
            mover_jogador('a')
        elif keyboard.is_pressed('d'):
            mover_jogador('d')

        if mover_inimigos():
            break
        
        exibir_mapa()
        
        time.sleep(0.4)

if __name__ == "__main__":
    jogar()
