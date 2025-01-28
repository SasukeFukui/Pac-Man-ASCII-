import jogar as j
import os
import show_score as s
import mov_choices as mc

#funcao pra iniciar as opcoes
def main():

    while True:
        sla = mc.screen()
        
        if sla == 0:
            j.jogar()
            
        elif sla == 1:
            s.mostrame()

        else:
            os._exit(0)
        

            
        

    
    