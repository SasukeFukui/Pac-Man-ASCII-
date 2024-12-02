import numpy as np
import os
import random

mapa = np.array([
    ["#","#","#","#","#","#","#","#","#"],
    ["#"," "," "," "," "," "," "," ","#"],
    ["#","#","#","#","#","#","#","#","#"]
])

def exibir_mapa():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para atualização do mapa
    for linha in mapa:
        print("".join(linha))  # Junta os caracteres da linha em uma string

def spawn_player():
    pos_x = random.randint(1,len(mapa)-1)
    pos_y = random.randint(1,len(mapa[1])-1)
    if mapa[pos_x,pos_y]==' ':
        mapa[pos_x,pos_y] ='c'
        exibir_mapa()
    else:
        spawn_player()

def spawn_fantasma():
    pos_x = random.randint(1,len(mapa)-1)
    pos_y = random.randint(1,len(mapa[1])-1)
    if mapa[pos_x,pos_y]==' ':
        mapa[pos_x,pos_y] ='f'
        exibir_mapa()
    else:
        spawn_fantasma()



spawn_player()
spawn_fantasma()
exibir_mapa()
