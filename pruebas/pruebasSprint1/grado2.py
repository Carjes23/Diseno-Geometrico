from deBoor import calcularPuntoEnIntervalo
import numpy as np
import math as m
import matplotlib.pyplot as plt

# 3 puntos de control, cuadratica, solo primer intervalo en t = (0, 0.5)
# con 3 puntos es imposible recorrer todo el dominio
def prueba3PuntosGrado2Con1Intervalo():
  grado = 2
  points = np.array([[0,0], [1,1], [2, 1]])
  knots = np.array([0, 0, 0, 1.0, 1.0, 1.0])

  X = []
  Y = []
  inicial = knots[grado]
  final = knots[grado+1]
  dominio = np.linspace(inicial,final, 50)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(2, x, knots, points, grado)
    X.append(res[0])
    Y.append(res[1])

  plt.scatter(points[:,0], points[:,1],marker='X')
  plt.scatter(X,Y, color='purple', marker='+')
  plt.show()

# 4 puntos de control, cuadratica, se recorren los 2 intervalos: (0, 0.2) y (0.2, 0.3)
# Si entrego mas nodos de los necesarios, no se repiten los "ultimos 3"
def prueba4PuntosGrado2Con2IntervalosNodosInnecesarios():
  grado = 2
  points = np.array([[0,0], [1,1], [2, 1], [3, 0]])
  knots = np.array([0, 0, 0, 0.2, 0.3, 0.4, 0.5, 1.0, 1.0, 1.0])

  X = []
  Y = []
  inicial = knots[grado]
  final = knots[grado+1]
  dominio = np.linspace(inicial,final, 20)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(2, x, knots, points, grado)
    X.append(res[0])
    Y.append(res[1])

  X2 = []
  Y2 = []
  inicial = knots[grado+1]
  final = knots[grado+2]
  dominio = np.linspace(inicial,final, 20)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(3, x, knots, points, grado)
    X2.append(res[0])
    Y2.append(res[1])

  plt.scatter(points[:,0], points[:,1],marker='X')
  plt.scatter(X,Y, color='purple', marker='+')
  plt.scatter(X2,Y2, color='red', marker='+')
  plt.show()


# 4 puntos de control, cuadratica, solo primer intervalo en t: (0, 0.2) y (0.2, 1.0)
# ahora si se puede recorrer todo el dominio
def prueba4PuntosGrado2Con2Intervalos():
  grado = 2
  points = np.array([[0,0], [1,1], [2, 1], [3, 0]])
  knots = np.array([0, 0, 0, 0.2, 1.0, 1.0, 1.0])

  X = []
  Y = []
  inicial = knots[grado]
  final = knots[grado+1]
  dominio = np.linspace(inicial,final, 20)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(2, x, knots, points, grado)
    X.append(res[0])
    Y.append(res[1])

  X2 = []
  Y2 = []
  inicial = knots[grado+1]
  final = knots[grado+2]
  dominio = np.linspace(inicial,final, 20)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(3, x, knots, points, grado)
    X2.append(res[0])
    Y2.append(res[1])

  plt.scatter(points[:,0], points[:,1],marker='X')
  plt.scatter(X,Y, color='purple', marker='+')
  plt.scatter(X2,Y2, color='red', marker='+')
  plt.show()

prueba3PuntosGrado2Con1Intervalo()
prueba4PuntosGrado2Con2Intervalos()
prueba4PuntosGrado2Con2IntervalosNodosInnecesarios()
