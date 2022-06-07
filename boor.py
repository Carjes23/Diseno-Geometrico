import numpy as np

class Boor:
    def __init__(self, controlPoints, nodos, grado):
        self.controlPoints = np.array(controlPoints)
        self.nodos = np.array(self.ampliarNodos(nodos, grado))
        self.grado = grado
        self.num_divisiones = len(self.nodos)
        return
    
    def ampliarNodos(self, nodos, grado):
        primerElemento = nodos[0]
        ultimoElemento = nodos[-1]
        for i in range(grado):
            nodos.insert(0,primerElemento)
            nodos.append(ultimoElemento)
        return nodos

    def calcularPuntos(self):
        xs = []
        ys = []
        maxpoints = len(self.nodos) #maxima cantidad de nodos
        for rango in range(self.grado,maxpoints-self.grado-1):
            divisiones = np.linspace(self.nodos[rango],self.nodos[rango+1],self.num_divisiones)      
            for punto in divisiones:
                result = self.calcularPuntosEnIntervalo(rango, punto, self.nodos, self.controlPoints, self.grado)
                xs.append(result[0])
                ys.append(result[1])
        return (xs,ys)

    def calcularPuntosEnIntervalo(self, k, x, t, c, p):
        """
        Argumentos
        ----
        k: indice del intervalo del nodo que contiene a x
        x: posicion
        t: matriz de posiciones de nodos
        c: matriz de puntos de control
        p: grado del B-spline
        """
        d = [c[j + k - p] for j in range(0, p+1)]

        for r in range(1, p+1):
            for j in range(p, r-1, -1):
                alpha = (x - t[j+k-p]) / (t[j+1+k-r] - t[j+k-p])
                d[j] = (1.0 - alpha) * d[j-1] + alpha * d[j]

        return d[p]