from turtle import color
from xml.etree.ElementTree import PI
from matplotlib import pyplot as plt
import numpy as np
from bsplines import *
from boor import Boor
from draggable_plot import * 

def calcularInvNTNyNT(l, p, T, m, U, n):
    N = np.zeros(((m-1,n - l - 1)))

    for i in range(0, m -1):
      for k in range(0, n - l - 1):
        N[i][k] = basisFunction(k + 1, p, T[i + 1], U)

    N = np.array(N)
    NT = np.transpose(N)
    NTN = np.dot(NT, N)
 
    invNTN = np.linalg.inv(NTN)

    return [invNTN, NT]

p = int(input("Dé el grado del B-Spline: "))
n = int(input("Mayor índice de puntos de control: "))

if __name__ == "__main__":
    plot = DraggablePlotExample()
    dictionary = plot.get_points()
Q = [] 
for key, val in dictionary.items(): 
    Q.append([key, val]) 
 
Q = np.array(Q) #Puntos de control Q escogidos en la parte interactiva de la gráfica

k = 0
l = 0

T = calculaT(Q)

m = len(Q) -1

U = calcularU(k, l, T, p, m, n)

[invNTN,NT] = calcularInvNTNyNT(l, p, T, m, U, n)

R = np.dot(NT,Q[1:-1])

numElemen = len(Q)
Pi = np.dot(invNTN,R)
P = np.zeros((n+1,2), float)
contElement = 0
for i in range(len(P)): #implementación sin derivadas para parte interactiva
  if i == 0:
    for j in range(len(P[i])):
      P[i][j] = Q[i][j]
  elif i == len(P)-1:
    for j in range(len(P[i])):
      P[-1][j] = Q[-1][j]
  else:
    for j in range(len(P[i])):
      P[i][j] = Pi[contElement][j]
    contElement += 1

grado = p
U = U[p:-p] #Reducción puntos repetidos

(X, Y) = Boor(grado, P, U)
plt.scatter(P[:,0], P[:,1],marker='o', color = 'black', label="Puntos de control") 
plt.scatter(Q[:,0], Q[:,1],marker='X', color = 'green', label="Datos Q") 
plt.plot(X,Y, color='purple', label="Curva B-spline") 
plt.legend(loc="best")
plt.title("Curva B-spline")
plt.show()

