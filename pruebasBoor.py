import matplotlib.pyplot as plt

from repositorioDatos import RepositorioDatos
from boor import Boor

repo = RepositorioDatos()
controlPoints = repo.obtenerPuntosControl()
nodos = repo.obtenerNodos()

gradoBSpline = int(input("Grado del B-Spline: "))

boor = Boor(controlPoints, nodos, gradoBSpline)
(xs, ys) = boor.calcularPuntos()

cxs = [controlPoints[i][0] for i in range(len(controlPoints))]
cys = [controlPoints[i][1] for i in range(len(controlPoints))]
plt.plot(cxs, cys, color = "black")
plt.plot(cxs, cys, "s")
plt.plot(xs, ys)
plt.show()
