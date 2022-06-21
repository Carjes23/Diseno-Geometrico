import matplotlib.pyplot as plt
import numpy as np
from math import floor

def calculaT(Q): #Parametrización de los datos Q ingresados
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

def calcularU(k, l, T, p, m, n): #Cálculo del vector de nodos
    U = [0.0 for i in range(0, (n + p + 1) + 1)]
    for i in range(0, p + 1): #Multiplicidad según el grado en el primer y último nodo
      U[i] = T[0]
      U[n + i + 1] = T[m]

    nc = n - k - l 
    try:
      inc = (m + 1)/(nc + 1)
    except:
      print("Número de puntos de control menor a total de derivadas")
      exit()
    low = high = 0
    d = -1
    W = [0.0 for i in range(0, nc + 1)]

    for i in range(0, nc + 1):
      d = d + inc
      high = floor(d + 0.5)
  
      sum = 0.0
      for j in range(low, high + 1):
        sum += T[j]

      try:
        W[i] = sum / (high - low + 1)  
      except:
        print("Número inválido de puntos escogidos interactivamente para el grado dado")
        exit()
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


def basisFunction(i, p, t, U):
  if p == 0:
    if U[i] <= t and t < U[i+1]:
      return 1
    return 0

  a = 0.0
  den1 = U[i+p] - U[i]
  if den1 != 0 :
    num1 = t - U[i]
    a = num1 / den1
  
  b = 0.0
  den2 = U[i+p+1]-U[i+1]
  if den2 != 0:
    num2 = U[i+p+1]-t
    b = num2 / (den2)
  
  return a* basisFunction(i, p-1, t, U) + b* basisFunction(i + 1, p - 1, t, U)

def derivada(i, p, j, u, U):
  if j == 0:
    aux = basisFunction(i, p, u, U)
    return aux

  den1 = U[i+p] - U[i]
  a1 = 0.0
  if den1 != 0:
    num1 = derivada(i, p-1, j-1, u, U)
    a1 = num1/den1
  
  den2 = U[i+p+1] - U[i+1]
  a2 = 0.0
  if den2 != 0:
    num2 = derivada(i+1, p-1, j-1, u, U)
    a2 = num2/den2

  res = p*(a1 - a2)
  return res

def findSpan(n, p, u, U):
  if u > U[n]:
    print(f'ERROR, intenta buscar un elemento "{u}" que es mayor a toda la lista de nodos')
    exit()
  if u < U[p]:
    print(f'ERROR, intenta buscar un elemento "{u}" que es menor a toda la lista de nodos')
    exit()
  if u == U[n]:
    return n
  
  low = p
  high = n + 1
  mid = int((low + high)/2)
  while( u < U[mid] or u >= U[mid + 1]):
    if u < U[mid]:
      high = mid
    else:
      low = mid

    mid = int((low + high)/2)
  return mid

def graficar(arreglo):
  plt.scatter(arreglo[:,0], arreglo[:,1])
  plt.show()

def ampliarNodos(nodos, grado):
    primerElemento = nodos[0]
    ultimoElemento = nodos[-1]
    for i in range(grado):
        nodos.insert(0,primerElemento)
        nodos.append(ultimoElemento)
    return nodos
