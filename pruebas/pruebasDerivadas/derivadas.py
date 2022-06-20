from bsplines import basisFunction

U = [0, 0, 0, 1, 2, 3, 4, 4, 5, 5, 5]

P = [0.0 for i in range(len(U) - 2)]
#P[0] = Q[0]

p = 2
n = len(U) - p - 2
u = 5/2

# j derivada
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

i = 4
p = 2
j = 2
u = 5/2
resultado = derivada(i, p, j, u, U)