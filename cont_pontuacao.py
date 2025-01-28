#funcao para fazer track dos pontos, enviar pontuacao e exibir.

pontuacao = 0
def conta_ponto(pontos):
    global pontuacao
    pontuacao+=pontos

def getpontuacao():
    return pontuacao

def exib_pontos():
    print("Sua pontuação: ",pontuacao)