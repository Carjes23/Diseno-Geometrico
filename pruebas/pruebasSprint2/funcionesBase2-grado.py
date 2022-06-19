import matplotlib.pyplot as plt
import numpy as np
from bsplines import findSpan
from bsplines import basisFunction

#pag 50 libro guia
#i-esimo funcion base B-spline de 2-grado (orden 2+1 = 3)

U = [0, 0, 0, 1, 2, 3, 4, 4, 5, 5, 5]
p = 2
n = len(U) - p - 1


maximo = 5
num = 100
# N_{i1}, variamos el i
N = [[]*num]*7

for i in range(1, 7+1):
  j = 0
  X = []
  Y = []
  for u in np.linspace(0, maximo, num):
    y = basisFunction(i, p, u, U )
    if y != 0.0:
      X.append(u)
      Y.append(y)
  plt.scatter(X, Y, marker = '.', label = f'N_{i}{p}')  

plt.legend(loc="upper right")
plt.text(0, 1.7, 'Figura 2.6 del libro guia', fontsize = 12)
plt.text(0, 1.3, 'Los puntos no graficados tienen y = 0', fontsize = 10)
plt.ylim(0, 2.0)
plt.show()