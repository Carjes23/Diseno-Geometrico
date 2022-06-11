import numpy as np
import matplotlib.pyplot as plt

def Boor(grado, puntos, nodos, numPuntosPorIntervalo = 20):

  numNodos = len(nodos)
  numIntervalosRealesMenos1 = len(nodos) - 2

  nodosAmpliados = ampliarNodos(nodos, grado)
  nodosAmpliados = np.array(nodosAmpliados)

  puntos = np.array(puntos)
  numPuntosControl = len(puntos)

  #TODO: Lanzar excepcion
  minNumeroPuntosControl= grado + 1
  if minNumeroPuntosControl > numPuntosControl:
    print(f'ERROR minimo numero de puntos de control es (grado + 1): {grado + 1}')
    exit()
  
  #TODO: Lanzar excepcion
  numValidoNodos = numPuntosControl + 1 - grado
  if numNodos != numValidoNodos:
    print(f'El numero valido de nodos es: (numPuntosControl + 1 - grado): {numPuntosControl + 1 - grado}')
    exit()

  X = []
  Y = []
  for indiceNodo in range(grado, (grado + numIntervalosRealesMenos1) + 1):
    inicial = nodosAmpliados[indiceNodo]
    final = nodosAmpliados[indiceNodo+1]
    dominio = np.linspace(inicial,final, numPuntosPorIntervalo)
  
    for x in dominio:
      res = calcularPuntoEnIntervalo(indiceNodo, x, nodosAmpliados, puntos, grado)
      X.append(res[0])
      Y.append(res[1])
  
  return (X, Y)
       
def ampliarNodos(nodos, grado):
    primerElemento = nodos[0]
    ultimoElemento = nodos[-1]
    for i in range(grado):
        nodos.insert(0,primerElemento)
        nodos.append(ultimoElemento)
    return nodos

def calcularPuntoEnIntervalo(i: int, x: int, nodos, c, grado: int):
    """Evaluates S(x).

    Arguments
    ---------
    i: Index of knot interval that contains x.
    x: Position.
    nodos: Array of knot positions, needs to be padded as described above.
    c: Array of control points.
    grado: Degree of B-spline.
    """
    d = [c[j + i - grado] for j in range(0, grado + 1)]

    for r in range(1, grado + 1):
        for j in range(grado, r - 1, -1):
            alpha = (x - nodos[j + i - grado]) / (nodos[j + 1 + i - r] - nodos[j + i - grado])
            d[j] = (1.0 - alpha) * d[j - 1] + alpha * d[j]

    return d[grado]