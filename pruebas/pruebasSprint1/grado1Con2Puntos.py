from matplotlib import markers
from deBoor import calcularPuntoEnIntervalo
import numpy as np
import math as m
import matplotlib.pyplot as plt

# 2 puntos de control
def prueba2PuntosGrado1():
  grado = 1
  points = np.array([[0,0], [1,1]])
  knots = np.array([1, 1, 2.0, 2.0])

  X = []
  Y = []
  inicial = knots[grado]
  final = knots[grado+1]
  dominio = np.linspace(inicial,final, 5)
  
  for x in dominio:
    res = calcularPuntoEnIntervalo(1, x, knots, points, grado)
    X.append(res[0])
    Y.append(res[1])

  plt.scatter(points[:,0], points[:,1],marker='X')
  plt.scatter(X,Y, color='purple', marker='+')
  plt.show()

prueba2PuntosGrado1()