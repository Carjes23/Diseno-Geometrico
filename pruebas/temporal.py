
#points = np.array([[i, m.sin(i)] for i in range(0, 11)])
points = np.array([[0,0], [1,1], [2,0]])
#knots = np.array([0, 0, 0, 0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.0, 1.0, 1.0])
knots = np.array([1, 1, 1.2, 1.3, 1.5, 2.0, 2.0])
p = 1

def evaluar(x):
  d00 = np.array([0, 0])
  d10 = np.array([1, 1])
  d20 = np.array([2, 0])

  #usando np para los calculos

  t = np.array([0, 0, 0.5, 1, 1])
  k = 2

  def calcW(x, t, j, l):
    div = (x - t[j])/(t[j+k-(r-1)]-t[j])
    return div

  # numero de puntos de control - 1 
  n = len(t) - 1

  w = np.empty((3,3))

  j = 1
  r = 1
  l = k - (r - 1) # 2 - (1 - 1) = 2
  #w[j][l] = calcW(x, t, j, k, r) # w12
  w12 = calcW(x, t, j, k, r)

  j = 2
  r = 2
  l = k - (r - 1) # 2 - (2-1) = 1
  #w[j][l] = calcW(x, t, j, k, r) # w21
  w21 = calcW(x, t, j, k, r) # w21

  j = 2
  r = 1
  l = k - (r - 1) # 2
  #w[j][l] = calcW(x, t, j, k, r) # w22
  w22 = calcW(x, t, j, k, r) # w22

  print(f'w12: {w12}')
  print(f'w21: {w21}')
  print(f'w22: {w22}')

  d = np.empty((3,3))

  j = 1
  r = 1
  #d[j][r] = (1 - w[j][k-(r-1)])*d00 + w[j][k-(r-1)]*d10
  d11 = (1 - w12)*d00 + w12*d10
  print(f'd11: {d11}')

  j = 2
  r = 1
  #d[j][r] = (1 - w[j][k-(r-1)])*d10 + w[j][k-(r-1)]*d20
  d21 = (1 - w22)*d10 + w22*d20
  print(f'd21: {d21}')

  j = 2
  r = 2
  #d[j][r] = (1 - w[j][k-(r-1)])*d[1][1] + w[j][k-(r-1)]*d[2][0]
  d22 = (1 - w21) * d11 + w21 * d21
  print(f'd22: {d22}')

  #print(f'd11: {d11}')
  #print(f'd21: {d21}')
  #print(f'd22: {d22}')

  return d22

  # w12 = (t-t[1])/(t[3]-t[1])
  # w22 = (t-t[2])/(t[4]-t[2])
  # d11 = (1-w())*d00 + w21*d10
  # d21 = (1-w12)*d10 + w12*d20

  # w21 = (t-t[2])/(t[3]-t[2])
  # d22 = (1-w21)*d11 + w21*d21
  # print(f'NP d22: {d22}')

  # # a mano
  # d22 = 0.72*d00 + 0.24*d10 +0.4*d20
  # print(d22)

# cant_divisiones = 100
# X = []
# Y = []
# maxpoints = len(knots) #maxima cantidad de nodos
# for rango in range(p,maxpoints-p-1):
#     divisiones = np.linspace(knots[rango],knots[rango+1],cant_divisiones)      
#     for punto in divisiones:
#         result = calcularPuntosEnIntervalo(rango, punto, knots, points, p)
#         X.append(result[0])
#         Y.append(result[1])