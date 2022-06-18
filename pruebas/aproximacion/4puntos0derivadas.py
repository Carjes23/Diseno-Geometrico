from math import floor
from matplotlib import pyplot as plt
import numpy as np
from bsplines import basisFunction
from boor import Boor

def calculaT(Q):
  m = len(Q) - 1
  T = [0.0 for i in range(m+1)]

  d = 0.0
  for r in range(1, m + 1):
    diff = Q[r] - Q[r-1]
    d += np.sqrt(diff.dot(diff))

  # print(f'd: {d}')

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

def calcularInvNTN(l, p, T, m, U):
    n = len(U) - p - 2
    print(f'n: {n}')
    print(f'm: {m}')
    N = [[0.0 for j in range(n - l - 1)] for i in range(m-1)]
    print(f'Creacion N: {N}')
    for i in range(0, m -1):
      for k in range(0, n - l - 1):
        N[i][k] = basisFunction(k + 1, p, T[i + 1], U)
        print(f'N_{i + 1}_{k + 1}: {N[i][k]}')

    N = np.array(N)
    NT = np.transpose(N)
    NTN = np.matmul(NT, N)
    #print(f'NTN: {NTN}')
    invNTN = np.linalg.inv(NTN)
    #print(f'invNTN: {invNTN}')
    return invNTN



Q = np.array([[0, 0], [1, 1], [2, 1.5], [3, 0]])
#Q = np.array([[0, 0], [1, 0], [3, 0], [8, 0]])

i = 0
l = 0
p = 2

T = calculaT(Q)
#print(f'T: {T}')
m = len(Q) -1

# n es el indice m'as alto de los puntos de control
# como no hay derivadas, entonces coincide con n
n = m

U = calcularU(i, l, T, p, m, n)
print(len(U))
print(f'U: {U}')

invNTN = calcularInvNTN(l, p, T, m, U)
# como no hay derivadas R, Q

# Quito el primer y ultimo elementos, P_0 = Q_0, P_3 = Q_3
# R = Q.copy()
# R = [[0.0 for i in range(k + 1, m)] for j in range(n-l-k-1)]
# print(f'R: {R}')

# R1 = Q1, R2 = Q2
P0 = Q[0]
P1 = invNTN[0][0] * Q[1] + invNTN[0][1] * Q[2]
P2 = invNTN[1][0] * Q[1] + invNTN[1][1] * Q[2]
P3 = Q[3]



P = np.array([[P0], [P1], [P2], [P3]])

print(f'U: {U}')
print(f'P: {P}')
grado = 2
P = [[0.0, 0.0],[-2.14609141, -0.7251314],[6.19599911, 3.93651934],[3.0, 0.0]]
U = [0.0, 0.4551833913647956, 1.0]

(X, Y) = Boor(grado, P, U)

plt.scatter(Q[:,0], Q[:,1],marker='X')
plt.scatter(X,Y, color='purple', marker='+')
plt.show()

# # N_{1}(t_1)
# k = findSpan(n, p, T[1], U)
# N11 = basisFunction(k, p, T[1], U)
# #print(f'N_{k-p}(1): {N11}')
# print(f'N_{k}(1): {N11}')

# # N_{2}(t_1)
# k = findSpan(n, p, T[1], U)
# N21 = basisFunction(k, p, T[1], U)
# #print(f'N_{k-p}(1): {N21}')
# print(f'N_{k}(1): {N21}')

# # N_{1}(t_2)
# k = findSpan(n, p, T[2], U)
# N12 = basisFunction(k, p, T[2], U)
# #print(f'N_{k-p}(2): {N12}')
# print(f'N_{k}(2): {N12}')

# # N_{2}(t_2)
# k = findSpan(n, p, T[2], U)
# N22 = basisFunction(k, p, T[2], U)
# #print(f'N_{k-p}(2): {N22}')
# print(f'N_{k}(2): {N22}')

# # N_{1}(t_3)
# k = findSpan(n, p, T[3], U)
# N13 = basisFunction(k, p, T[3], U)
# #print(f'N_{k-p}(3): {N13}')
# print(f'N_{k}(3): {N13}')

# # N_{2}(t_3)
# k = findSpan(n, p, T[3], U)
# N23 = basisFunction(k, p, T[3], U)
# #print(f'N_{k-p}(3): {N23}')
# print(f'N_{k}(3): {N23}')

# print([[N11, N21], [N12, N22], [N13, N23]])
# N = np.array([[N11, N21], [N12, N22], [N13, N23]])
# NT = np.transpose(N)
# NTN = np.matmul(NT, N)
# invNTN = np.invert(NTN)

# print(invNTN)