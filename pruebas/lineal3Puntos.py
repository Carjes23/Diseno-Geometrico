from deBoor import calcularPuntoEnIntervalo
import numpy as np
import math as m
import matplotlib.pyplot as plt

# 3 puntos de control lineal
def prueba3PuntosLineal():
  points = np.array([[0,0], [1,1], [2,0]])

  # da la misma grafica si uso, creo que por ser lineal
  #knots = np.array([0, 0, 5, 10, 10])
  knots = np.array([0, 0, 1, 10, 10])
  
  grado = 1
  inicial = knots[grado]
  final = knots[grado+1]
  dominio = np.linspace(inicial,final, 10)
  
  X = []
  Y = []
  for x in dominio:
    res = calcularPuntoEnIntervalo(grado, x, knots, points, grado)
    X.append(res[0])
    Y.append(res[1])

  inicial = knots[grado+1]
  final = knots[grado+2]
  dominio = np.linspace(inicial,final, 10)
  X2 = []
  Y2 = []
  for x in dominio:
    res = calcularPuntoEnIntervalo(grado+1, x, knots, points, grado)
    X2.append(res[0])
    Y2.append(res[1])


  plt.scatter(points[:,0], points[:,1],marker='X')
  plt.scatter(X,Y, color='black', marker='+')
  plt.scatter(X2,Y2, color='red', marker='+')
  plt.show()

prueba3PuntosLineal()
