import numpy as np
from math import floor, ceil
from boor import Boor
def aproxDeNodos(t,m,n,p,k,l):
    """Argumentos
    ---------
    t: Parámetros ingresados en forma de lista.
    #TODO: Resolver el significado de m.
    m: Último parámetro.
    n: Mayor índice de los puntos de control.
    p: Grado del B-spline.
    k: Mayor grado de la derivada del primer parámetro.
    l: Mayor grado de la derivada del último parámetro 
    """
    U = np.zeros(n+p+2) #Se inicializa el vector de nodos
    for i in range(0,p+1):
        U[i] = t[0]
        U[n+i+1] = t[-1]
    nc = n-k-l
    inc = (m+1)/(nc+1)
    low = 0
    high = 0
    d = -1
    w = np.zeros(nc+1) 
    for i in range(0,nc+1):
        d = d + inc
        high= floor(d+0.5)
        sum = 0
        for j in range(low,high+1):
            sum += t[j]
        w[i] = sum/(high-low+1)
        low = high + 1

    iss = 1 - k
    ie = nc - p + l
    r = p
    for i in range(iss, ie+1):
        js = max(0,i);
        je = min(nc,i+p-1)
        r += 1
        sum = 0
        for j in range(js,je+1):
            sum += w[j]
        U[r] = sum / (je-js+1)
    return U

def estDerivadas(t,m,n,p,k,l):
    mh = m/2
    tp = ceil((p+1)*((m+1)/(n+1)))
    iss = max(mh,m-tp)
    ie = min(mh,tp)
    ml = m-iss+ie
    nl = ceil(n*((ml)/m))
    s = []
    s.append(0)
    i = int(iss+1)
    j = 1
    while j <= ml:
        s.append(s[j-1]+t[i]-t[i-1])
        if i == m:
            i = 0
            idd = j
        i += 1
        j += 1
    return s

# def matriz(t,m,n,p,k,l):
#     rj = p;
#     sj = p-k-1;
#     ej = -2-k;
#     nd = n-k-l-2;
#     N= np.zeros(m-1,p)
#     for i in range (0, m-1): #Pregunta
#         for j in range (0, p):
#             N[i][j] = 0
#     start=[]
#     end=[]
#     for i in range (0, nd):
#         start[i] = 0
#         end[i] = m-2
#     for i in range (1, m-1):
#         #j ← span index of [uj,uj+1) ti is in
#     li = max(j-p,k + 1);
#     hi = min(j,n-l-1);
#     #put Nli,. . .,Nhi in matrix left padded;
#     #index[i − 1] = max(0,j − p − k − 1);
#     if(j > rj):
#     for kk in range (1, j-rj):
#         sj = sj + 1 
#         ej = ej + 1
#     if(sj <= nd):
#         start[sj] = i-1
#     if(ej >= 0): 
#         end[ej] = i-2




def deBoor(k: int, x: int, t, c, p: int):
    """Argumentos
    ---------
    i: Índice del intervalo de nodos que contiene a las x.
    x: Posición.
    nodos: Colección (array) de las posiciones de los nodos.
    c: Colección (array) de puntos de control.
    grado: Grado del B-spline.
    """
    d = [c[j + k - p] for j in range(0, p + 1)]

    for r in range(1, p + 1):
        for j in range(p, r - 1, -1):
            alpha = (x - t[j + k - p]) / (t[j + 1 + k - r] - t[j + k - p])
            d[j] = (1.0 - alpha) * d[j - 1] + alpha * d[j]

    return d[p]

para = [i for i in range(0,31)]
knots = aproxDeNodos(para,30,9,3,2,2)
points = estDerivadas(para,30,9,3,2,2)
print(len(knots), len(points))
p = 3
cant_divisiones = 20
X = []
Y = []
print(para)
print(knots)
print(points)
# trazadores = []
# maxpoints = len(knots) #maxima cantidad de nodos
# for rango in range(p,maxpoints-p-1):
#     divisiones = np.linspace(knots[rango],knots[rango+1],cant_divisiones)      
#     for punto in divisiones:
#         result = deBoor(rango, punto, knots, points, p)
#         print(result)
#         X.append(result[0])
#         Y.append(result[1])
# plt.plot(points[:,0], points[:,1],'.')
# plt.plot(X,Y)
# plt.show()