import keyboard
import time
from exibMapa import exibir_mapa
import mov_player as mp
from spawns import spawn_player,spawn_pontos,spawn_inimigo
from iniamigos import mover_inimigos    


#funcao para iniciar o jogo
def jogar():
        
    spawn_inimigo()
    spawn_player()
    spawn_pontos()
    exibir_mapa()
    global name
    name = input("Digite seu nick: ")
    global modo
    modo = int(input("Escolha o modo de jogo=====> (1)(2)"))  
    global stime 
    stime = time.time()

    if modo ==1:
        
        modo = 1
        clk = 0.5
    else:
        modo = 2
        clk = 0.1
    
    while True:
        if keyboard.is_pressed('w'):
            mp.mover_jogador('w')
        elif keyboard.is_pressed('s'):
            mp.mover_jogador('s')
        elif keyboard.is_pressed('a'):
            mp.mover_jogador('a')
        elif keyboard.is_pressed('d'):
            mp.mover_jogador('d')

        if mover_inimigos():
            break
        
        exibir_mapa()
        
        time.sleep(clk)

#funcoes para enviar variavel

def getModojogo():
    return modo
    
def getstartime():
    return stime
def getname():
    return name

