import matplotlib.pyplot as plt
import numpy as np

from repositorioDatos import RepositorioDatos
from boor import Boor

repo = RepositorioDatos()
puntos = repo.obtenerPuntosControl()
nodos = repo.obtenerNodos()
grado = int(input("Grado del B-Spline: "))

if len(puntos[0]) ==2:
    (xs, ys) = Boor(grado, puntos, nodos, 50)
    cxs = [puntos[i][0] for i in range(len(puntos))]
    cys = [puntos[i][1] for i in range(len(puntos))]
    plt.plot(cxs, cys, color = "black") #Polinomio de control
    plt.plot(cxs, cys, "s")
    plt.plot(xs, ys) #Curva B-spline en dos dimensiones
    plt.show()
else:
    (xs, ys, zs) = Boor(grado, puntos, nodos, 50)
    cxs = [puntos[i][0] for i in range(len(puntos))]
    cys = [puntos[i][1] for i in range(len(puntos))]
    czs = [puntos[i][2] for i in range(len(puntos))]
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    xs = np.array([xs])
    ys = np.array([ys])
    zs = np.array([zs])
    ax1.plot_wireframe(xs, ys, zs) #Curva B-spline en tres dimensiones
    plt.plot(cxs, cys, cys, "s")
    plt.plot(cxs, cys, czs, color = "black") #Polinomio de control
    plt.show()