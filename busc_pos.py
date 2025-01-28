import numpy as np
from exibMapa import mapa

#funcao para buscar posicao...
def encontrar_posicao(simb):
    result = np.where(mapa == simb)
    if result[0].size > 0:
        return result[0][0], result[1][0]
    return None

print(encontrar_posicao('①'))