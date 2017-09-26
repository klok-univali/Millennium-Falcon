import math

#
# Função 'disTwoPoints(p1, p2)' retorna a distância entre dois pontos
#
# @param1 - Vetor de 2 posições com as coordenadas do primeiro ponto
# @param2 - Vetor de 2 posições com as coordenadas do primeiro ponto
#
# @return - distância entre @param1 e @param2
#
def disTwoPoints(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

#
# Função 'timeForVel(v0, v1, a)' retorna o tempo para sair da velocidade 1 e atingir a velocidade 2 com a aceleração informada
#
# @param1 - Velocidade inicial
# @param2 - Velocidade final
# @param3 - Aceleração
#
# @return - Tempo necessário para sair de @param1 até @param2 com a aceleração @param3
#
def timeForVel(v0, v1, a):
    return (v1 - v0)/a

#
# Função 'disMRUV(d0, v0, t, a)' retorna a distância percorrida em determinado tempo com certa aceleração.
#
# @param1 - Distância inicial
# @param2 - Velocidade inicial
# @param3 - Tempo
# @param4 - Aceleração
#
# @return - Distancia final
#
def disMRUV(d0, v0, t, a):
    return d0 + v0*t + (1/2)*a*t**2

#
# Função 'disMRU(v,t)' retorna a distancia percorrida com determinada velocidade em determinado tempo.
#
# @param1 - Velocidade
# @param2 - Tempo
#
# @return - Distancia percorrida
#
def disMRU(v, t):
    return v*t

#
# Função 'timeDisVel(d, v)' retorna o tempo necessário para percorrer a distancia na velocidade informada
#
# @param1 - Distância a percorrer
# @param2 - Velocidade
#
# @return - Tempo necessário para percorrer @param1 com a velocidade @param2
#
def timeDisVel(d, v):
    return d/v

#
# Função 'velMRUV(v0,a,t)' retorna a velocidade em determinado tempo com certa aceleração.
#
# @param1 - Velocidade inicial
# @param2 - Aceleração
# @param3 - Tempo
#
# @return - Velocidade no @param3 com aceleração @param2
#
def velMRUV(v0, a, t):
    return v0 + a*t

#
# Função 'coefAng(p1, p2)' retorna o coeficiente angular de reta entre dois pontos em radianos.
#
# @param1 - Vetor de 2 posições com as coordenadas do primeiro ponto
# @param2 - Vetor de 2 posições com as coordenadas do segundo ponto
#
# @return
#
def coefAng(p1, p2):
    return math.atan(((p2[1] - p1[1])/(p2[0]-p1[0])))

#
# Função 'updateCoord(d, m)' retorna o ponto após tem percorrido a distancia na reta informada.
#
# @param1 - Distância percorrida
# @param2 - Coeficiente angular da reta em radianos
#
# @return - Vetor com duas posições referente ao ponto descoberto.
#
def updateCoord(d, m):
    # return [d*math.cos(m), d*math.sin(m)]
    return [d * math.sin(m), d * math.cos(m)]
