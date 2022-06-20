from math import floor
from turtle import color
from xml.etree.ElementTree import PI
from matplotlib import pyplot as plt
import numpy as np
from bsplines import basisFunction
from boor import Boor
from draggable_plot import * 

def calculaT(Q):
  m = len(Q) - 1
  T = [0.0 for i in range(m+1)]

  d = 0.0
  for r in range(1, m + 1):
    diff = Q[r] - Q[r-1]
    d += np.sqrt(diff.dot(diff))


  for r in range(1, m+1):
    diff = Q[r] - Q[r-1]
    T[r] = T[r-1] +  np.sqrt(diff.dot(diff))/d

  return T

def calcularU(k, l, T, p, m, n):
    U = [0.0 for i in range(0, (n + p + 1) + 1)]
    for i in range(0, p + 1):
      U[i] = T[0]
      U[n + i + 1] = T[m]

    nc = n - k - l
    inc = (m + 1)/(nc + 1)
    low = high = 0
    d = -1
    W = [0.0 for i in range(0, nc + 1)]

    for i in range(0, nc + 1):
      d = d + inc
      high = floor(d + 0.5)
  
      sum = 0.0
      for j in range(low, high + 1):
        sum += T[j]

      W[i] = sum / (high - low + 1)  
      low = high + 1

    iS = 1 - k
    ie = nc - p  + l
    r = p
    for i in range(iS, ie + 1):
      js = max(0, i)
      je = min(nc, i + p - 1)
      r += 1

      sum = 0.0
      for j in range(js, je + 1):
        sum += W[j]
  
      U[r] = sum/(je - js + 1)
    
    return U

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
n = int(input("Índice mayor de puntos de control: "))

if __name__ == "__main__":
    plot = DraggablePlotExample()
    dictionary = plot.get_points()
Q = [] 
for key, val in dictionary.items(): 
    Q.append([key, val]) 
 
Q = np.array(Q)



i = 0
l = 0


T = calculaT(Q)

m = len(Q) -1


U = calcularU(i, l, T, p, m, n)

[invNTN,NT] = calcularInvNTNyNT(l, p, T, m, U, n)

R = np.dot(NT,Q[1:-1])


numElemen = len(Q)
Pi = np.dot(invNTN,R)
P = np.zeros((n+1,2), float)
contElement = 0
for i in range(len(P)): #implementación sin derivadas 
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

