import time
import keyboard
from exibMapa import exibir_mapa
from mov_player import mover_jogador
from spawns import spawn_player,spawn_pontos
from iniamigos import mover_inimigos    

def jogar():
    spawn_pontos()
    spawn_player()
    exibir_mapa()
    modo = input("Escolha o modo de jogo=====> (1)(2)")  
    
    if modo =='1':
        
        modo = 1
        clk = 0.5
    else:
        modo = 2
        clk = 0.1

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
        
        time.sleep(clk)

if __name__ == "__main__":
    
    name = input("Digite o nome do player: ")
    jogar()

    stime =  time.time()
    ftime = time.time()
    etime = ftime - stime