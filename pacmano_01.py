import numpy as np
import os

mapa = np.array([
    ["#","#","#","#","#","#"],
    ["#"," "," "," "," ","#"],
    ["#"," "," "," "," ","#"],
    ["#"," "," "," "," ","#"],
    ["#","#","#","#","#","#"]
])

def exibir_mapa():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para atualização do mapa
    for linha in mapa:
        print("".join(linha))  # Junta os caracteres da linha em uma string

exibir_mapa()