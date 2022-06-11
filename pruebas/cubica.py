from deBoor import calcularPuntoEnIntervalo
import numpy as np
import math as m
import matplotlib.pyplot as plt

# 4 puntos de control, cubica, 1 intervalo t = (0, 1)
def prueba4PuntosCuadratica1Intervalo():
  grado = 3
  points = np.array([[0,0], [-1,1], [1, 2], [2, 2]])
  knots = np.array([0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0])

  X = []
  Y = []
  inicial = knots[grado]
  final = knots[grado+1]
  dominio = np.linspace(inicial,final, 20)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(grado, x, knots, points, grado)
    X.append(res[0])
    Y.append(res[1])

  plt.scatter(points[:,0], points[:,1],marker='X')
  plt.scatter(X,Y, color='purple', marker='+')
  plt.show()

# 4 puntos de control, cubica, 1 intervalo t = (0, 1)
def prueba4PuntosCuadratica1Intervalo2():
  grado = 3
  points = np.array([[0,0], [-1,1], [1, 2], [2, 2], [3, 1], [4, 0]])
  knots = np.array([0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0])

  X = []
  Y = []
  inicial = knots[grado]
  final = knots[grado+1]
  dominio = np.linspace(inicial,final, 20)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(grado, x, knots, points, grado)
    X.append(res[0])
    Y.append(res[1])

  plt.scatter(points[:,0], points[:,1],marker='X')
  plt.scatter(X,Y, color='purple', marker='+')
  plt.show()

# 5 puntos de control, cubica, 2 intervalos t = (0, 0.5) y (0.5, 1)
def prueba5PuntosCuadratica2Intervalos():
  grado = 3
  points = np.array([[0,0], [-1,1], [1, 2], [2, 2], [3, 1], [4, 0]])
  knots = np.array([0, 0, 0, 0, 0.5, 1.0, 1.0, 1.0, 1.0])

  X = []
  Y = []
  inicial = knots[grado]
  final = knots[grado+1]
  dominio = np.linspace(inicial,final, 20)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(grado, x, knots, points, grado)
    X.append(res[0])
    Y.append(res[1])

  X2 = []
  Y2 = []
  
  inicial = knots[grado+1]
  final = knots[grado+2]
  dominio = np.linspace(inicial,final, 20)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(grado + 1, x, knots, points, grado)
    X2.append(res[0])
    Y2.append(res[1])

  plt.scatter(points[:,0], points[:,1],marker='X')
  plt.scatter(X,Y, color='purple', marker='+')
  plt.scatter(X2,Y2, color='red', marker='+')
  plt.show()

# 6 puntos de control, cubica, 2 intervalos t = (0, 0.5), (0.5, 0.7) y (0.7, 1.0)
def prueba6PuntosCuadratica3Intervalos():
  grado = 3
  points = np.array([[0,0], [-1,1], [1, 2], [2, 2], [3, 1], [4, 0]])
  knots = np.array([0, 0, 0, 0, 0.5, 0.7, 1.0, 1.0, 1.0, 1.0])

  X = []
  Y = []
  inicial = knots[grado]
  final = knots[grado+1]
  dominio = np.linspace(inicial,final, 20)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(grado, x, knots, points, grado)
    X.append(res[0])
    Y.append(res[1])

  X2 = []
  Y2 = []
  inicial = knots[grado+1]
  final = knots[grado+2]
  dominio = np.linspace(inicial,final, 20)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(grado + 1, x, knots, points, grado)
    X2.append(res[0])
    Y2.append(res[1])

  X3 = []
  Y3 = []
  inicial = knots[grado+2]
  final = knots[grado+3]
  dominio = np.linspace(inicial,final, 20)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(grado + 2, x, knots, points, grado)
    X3.append(res[0])
    Y3.append(res[1])

  plt.scatter(points[:,0], points[:,1],marker='X')
  plt.scatter(X,Y, color='purple', marker='+')
  plt.scatter(X2,Y2, color='red', marker='+')
  plt.scatter(X3,Y3, color='green', marker='+')
  plt.show()

prueba4PuntosCuadratica1Intervalo()
prueba4PuntosCuadratica1Intervalo2()
prueba5PuntosCuadratica2Intervalos()
prueba6PuntosCuadratica3Intervalos()