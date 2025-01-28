import jogar as j
from cont_pontuacao import getpontuacao
import time

#funcao para guardar score em arq bin
def score_guardado(nomeArq, condicao):
    
    with open(nomeArq, 'ab') as arquivo:  
      
        conteudo = f'\nPlayer: {j.getname()}'
        if condicao == 'venceu':
            conteudo += f'\nO jogador: {condicao}'
            ftime = time.time()
            tempo = round((ftime - j.getstartime()), 3)
            conteudo += f'\nTempo: {tempo}'
        else:
            conteudo += f'\nO jogador: {condicao}'

        conteudo += f'\nModo de jogo: {j.getModojogo()}'
        conteudo += f'\nPontos: {getpontuacao()}'
        score = getpontuacao() * j.getModojogo()
        score = round(score, 3)
        conteudo += f'\nScore: {score}'
        conteudo += '\n----------------------------------------'

        arquivo.write(conteudo.encode('utf-8'))

    print(f"Seu score foi: {score}")
    print("Score guardado")

