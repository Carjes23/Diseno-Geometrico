import matplotlib.pyplot as plt
import numpy as np

def basisFunction(i, p, t, T):
  if p == 0:
    if T[i] <= t and t < T[i+1]:
      return 1
    return 0

  a = 0.0
  den1 = T[i+p] - T[i]
  if den1 != 0 :
    num1 = t - T[i]
    a = num1 / den1
  
  b = 0.0
  den2 = T[i+p+1]-T[i+1]
  if den2 != 0:
    num2 = T[i+p+1]-t
    b = num2 / (den2)
  
  return a* basisFunction(i, p-1, t, T) + b* basisFunction(i + 1, p - 1, t, T)

U = [0, 1, 2]
N_1_0 = basisFunction(1, 0, 0.2, U)
print(N_1_0)


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

# TODO: Problemas al evaluar en el ultimo punto: u = 1.0
# U = [0, 0, 0, 1, 1, 1]
# p = 0
# n = len(U) - p - 1

# i = findSpan(n, p, 1.0, U)
# N = basisFunction(i, p, 1.0, U )
# print(f'N_{i}{p}({1.0}): {N}')