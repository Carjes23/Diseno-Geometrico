import matplotlib.pyplot as plt

from repositorioDatos import RepositorioDatos
from boor import Boor

repo = RepositorioDatos()
puntos = repo.obtenerPuntosControl()
nodos = repo.obtenerNodos()
grado = int(input("Grado del B-Spline: "))

# grado = 1
# # 7 puntos
# puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# # 7 nodos
# nodos = [0, 0.2, 0.4, 0.6, 0.8, 0.9, 1.0]

# grado = 2
# # 7 puntos
# puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# # 6 nodos
# nodos = [0, 0.2, 0.4, 0.7, 0.9, 1.0]
    
# grado = 3
# # 7 puntos
# puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# # 5 nodos
# nodos = [0, 0.2, 0.4, 0.7, 1.0]

# grado = 4
# # 7 puntos
# puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# # 4 nodos
# nodos = [0, 0.3, 0.6, 1.0]

grado = 5
# # 7 puntos
puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# # 3 nodos
nodos = [0, 0.3, 1.0]

#grado = 6
# # 7 puntos
#puntos = [[0,0], [-1,1], [1, 2], [2, 2], [3, 1.5], [4, 0], [2, -1]]
# 2 nodos
#nodos = [0, 1]


(xs, ys) = Boor(grado, puntos, nodos, 50)
cxs = [puntos[i][0] for i in range(len(puntos))]
cys = [puntos[i][1] for i in range(len(puntos))]
plt.plot(cxs, cys, color = "black")
plt.plot(cxs, cys, "s")
plt.plot(xs, ys)
plt.show()