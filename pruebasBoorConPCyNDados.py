import matplotlib.pyplot as plt

from repositorioDatos import RepositorioDatos
from boor import Boor

repo = RepositorioDatos()
puntos = repo.obtenerPuntosControl()
nodos = repo.obtenerNodos()
grado = int(input("Grado del B-Spline: "))

(xs, ys) = Boor(grado, puntos, nodos, 50)
cxs = [puntos[i][0] for i in range(len(puntos))]
cys = [puntos[i][1] for i in range(len(puntos))]
plt.plot(cxs, cys, color = "black")
plt.plot(cxs, cys, "s")
plt.plot(xs, ys)
plt.show()