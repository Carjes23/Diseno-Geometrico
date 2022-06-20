from math import floor
from matplotlib import pyplot as plt
import numpy as np
from bsplines import basisFunction
from boor import Boor
from draggable_plot import *
from repositorioDatos import RepositorioDatos

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

# def calcularInvNTNyNT(l, p, T, m, U, n):
#     N = np.zeros(((m-1,n - l - 1)))

#     for i in range(0, m -1):
#       for k in range(0, n - l - 1):
#         N[i][k] = basisFunction(k + 1, p, T[i + 1], U)

#     N = np.array(N)
#     NT = np.transpose(N)
#     NTN = np.dot(NT, N)
 
#     invNTN = np.linalg.inv(NTN)

#     return [invNTN, NT]



def calcularPuntDer(k,l, T, di, df, p, Q, U):
  p0= Q[0]
  print(p0)
  pm= Q[-1]
  print(pm)
  #p1= (1/basisFunction(1, p, T[0], U))*(di[0]-basisFunction(0, p, T[0], U)*Q[0])
  Pderi=[p0]
  Pderf=[pm]
  for i in range(1, k):
    suma= np.array([0,0])
    for j in range(0, i-1):
      suma+= basisFunction(j, p, T[0], U)*Pderi[j]
      
    print(suma) 
    Pderi.append((1/basisFunction(k, p, T[0], U))*(di[i]-suma))
    print(Pderi)


  # for m in range(1, l):
  #   for n in range(0,m-1):
  #           suma= basisFunction(n, p, T[-1], U)*Pderf[n]
      
  #   Pderf.append((1/basisFunction(k + 1, p, T[-1], U))*(df[m]-suma))





p = 3
n = 4

#Q = np.array([[0, 0], [1, 1], [2, 1.5], [3, 0],[4,2]])
repo = RepositorioDatos()
Q = repo.obtenerPuntosQ()
Q= np.array(Q)
k=2
l=2

T = calculaT(Q)

m = len(Q) -1

U = calcularU(k, l, T, p, m, n)

#[invNTN,NT] = calcularInvNTNyNT(l, p, T, m, U, n)

di=np.array([[1,2],[7,8]])
df=np.array([[2,3]])

pcderiv=calcularPuntDer(k,l, T, di, df, p, Q, U)

#R = np.dot(NT,Q[1:-1])


# numElemen = len(Q)
# Pi = np.dot(invNTN,R)
# P = np.zeros((n+1,2), float) #Pensar en automatizar 3 dimensiones.
# contElement = 0
# for i in range(len(P)): #implementación sin derivadas 
#   if i == 0:
#     for j in range(len(P[i])):
#       P[i][j] = Q[i][j]
#   elif i == len(P)-1:
#     for j in range(len(P[i])):
#       P[-1][j] = Q[-1][j]
#   else:
#     for j in range(len(P[i])):
#       P[i][j] = Pi[contElement][j]
#     contElement += 1
# grado = p
# U = U[p:-p] #Reducción puntos repetidos
# (X, Y) = Boor(grado, P, U)
# plt.scatter(P[:,0], P[:,1],marker='o', color = 'black', label="Puntos de control") 
# plt.scatter(Q[:,0], Q[:,1],marker='X', color = 'green', label="Datos Q") 
# plt.plot(X,Y, color='purple', label="Curva B-spline") 
# plt.legend(loc="best")
# plt.title("Curva B-spline")
# plt.show()
