from deBoor import calcularPuntoEnIntervalo
import numpy as np
import matplotlib.pyplot as plt

def pruebaNPuntos(grado, puntos, nodos, numPuntosPorIntervalo = 20):

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

  for indiceNodo in range(grado, (grado + numIntervalosRealesMenos1) + 1):
    X = []
    Y = []
    inicial = nodosAmpliados[indiceNodo]
    final = nodosAmpliados[indiceNodo+1]
    dominio = np.linspace(inicial,final, numPuntosPorIntervalo)
  
    for x in dominio:
      res = calcularPuntoEnIntervalo(indiceNodo, x, nodosAmpliados, puntos, grado)
      X.append(res[0])
      Y.append(res[1])
    
    plt.scatter(X,Y, marker='+')
  
  plt.scatter(puntos[:,0], puntos[:,1],marker='X')
  plt.show()

    
def ampliarNodos(nodos, grado):
    primerElemento = nodos[0]
    ultimoElemento = nodos[-1]
    for i in range(grado):
        nodos.insert(0,primerElemento)
        nodos.append(ultimoElemento)
    return nodos

grado = 1
# 7 puntos
puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# 7 nodos
nodos = [0, 0.2, 0.4, 0.6, 0.8, 0.9, 1.0]
pruebaNPuntos(grado, puntos, nodos)

grado = 2
# 7 puntos
puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# 6 nodos
nodos = [0, 0.2, 0.4, 0.7, 0.9, 1.0]
pruebaNPuntos(grado, puntos, nodos)
    
grado = 3
# 7 puntos
puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# 5 nodos
nodos = [0, 0.2, 0.4, 0.7, 1.0]
pruebaNPuntos(grado, puntos, nodos)

grado = 4
# 7 puntos
puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# 4 nodos
nodos = [0, 0.3, 0.6, 1.0]
pruebaNPuntos(grado, puntos, nodos)

grado = 5
# 7 puntos
puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# 3 nodos
nodos = [0, 0.3, 1.0]
pruebaNPuntos(grado, puntos, nodos)

grado = 5
# 7 puntos
puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# 2 nodos
nodos = [0, 1]
pruebaNPuntos(grado, puntos, nodos)

