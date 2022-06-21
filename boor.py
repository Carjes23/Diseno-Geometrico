import numpy as np
import matplotlib.pyplot as plt

def Boor(grado, puntos, nodos, numPuntosPorIntervalo = 20):

  numNodos = len(nodos)
  numIntervalosRealesMenos1 = len(nodos) - 2

  nodosAmpliados = ampliarNodos(nodos, grado)
  nodosAmpliados = np.array(nodosAmpliados)

  puntos = np.array(puntos)
  numPuntosControl = len(puntos)

  minNumeroPuntosControl= grado + 1
  if minNumeroPuntosControl > numPuntosControl:
    print(f'El mínimo número de puntos de control es (grado + 1)= {grado + 1}')
    exit()
  
  numValidoNodos = numPuntosControl + 1 - grado
  if numNodos > numValidoNodos:
    print(f'El número válido de nodos es igual o menor a (numPuntosControl + 1 - grado)= {numPuntosControl + 1 - grado} o menor')
    exit()

  X = []
  Y = []
  Z = []
  a=0
  for indiceNodo in range(grado, (grado + numIntervalosRealesMenos1) + 1):
    inicial = nodosAmpliados[indiceNodo]
    final = nodosAmpliados[indiceNodo+1]
    dominio = np.linspace(inicial,final, numPuntosPorIntervalo)
  
    for x in dominio:
      res = calcularPuntoEnIntervalo(indiceNodo, x, nodosAmpliados, puntos, grado)
      if len(res)>2:
        X.append(res[0])
        Y.append(res[1])
        Z.append(res[2])
        a=1
      else:
        X.append(res[0])
        Y.append(res[1])
  if a==1:
    return (X, Y, Z)
  else:
    return (X, Y)
       
def ampliarNodos(nodos, grado):
    try:
      primerElemento = nodos[0]
    except:
      print("Número inválido de puntos de control para el grado dado")
      exit()
    ultimoElemento = nodos[-1]
    for i in range(grado):
        nodos.insert(0,primerElemento)
        nodos.append(ultimoElemento)
    return nodos

def calcularPuntoEnIntervalo(i: int, x: int, nodos, c, grado: int):
    """Argumentos
    ---------
    i: Índice del intervalo de nodos que contiene a las x.
    x: Posición.
    nodos: Colección (array) de las posiciones de los nodos.
    c: Colección (array) de puntos de control.
    grado: Grado del B-spline.
    """
    d = [c[j + i - grado] for j in range(0, grado + 1)]

    for r in range(1, grado + 1):
        for j in range(grado, r - 1, -1):
            alpha = (x - nodos[j + i - grado]) / (nodos[j + 1 + i - r] - nodos[j + i - grado])
            d[j] = (1.0 - alpha) * d[j - 1] + alpha * d[j]

    return d[grado]