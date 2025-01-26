from pacfds import name,etime
from cont_pontuacao import pontuacao


def score_guardado(nomeArq,name, pontuacao, tmp):
    arquivo = open(nomeArq, 'a')
    arquivo.write(name+ '\n')
    arquivo.write(pontuacao, '\n')
    arquivo.write(tmp, '\n')
    arquivo.write('----------------------------------------')
    arquivo.close()
score_guardado('a', name, pontuacao, etime)