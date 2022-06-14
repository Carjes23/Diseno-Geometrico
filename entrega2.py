import numpy as np
from boor import Boor
def entrega2(t,m,n,p,k,l):
    U = np.zeros(n+p+2)
    for i in range(0,p+1):
        U[i] = t[0]
        U[n+i+1] = t[-1]
    nc = n-k-l
    inc = (m+1)/(nc+1)
    low = 0
    high = 0
    d = -1
    w = np.zeros(nc+5)
    for i in range(0,nc+1):
        d = d + inc
        if type(d) == int:
            high = d
        elif d >= 0:
            high = int(d)
        else:
            high = int(d)-1
        sum = 0
        for j in range(low,high+1):
            sum += t[j]
        w[i] = sum/(high-low)
        low = high + 1
    iss = 1 - k
    ie = nc - p + l
    r = p
    for i in range(iss, ie+1):
        js = max(0,i);
        je = min(nc,i+p-1)
        r += 1
        sum = 0
        for j in range(js+je+1):
            sum += w[j]
        U[r] = sum / (je-js+1)
    return U
def entrega22(t,m,n,p,k,l):
    mh = m/2
    tp = (p+1)*((m+1)/n+1)
    if type(tp) == int:
        tp = tp
    elif tp >= 0:
        tp = int(tp)+1
    else:
        tp = int(tp)
    iss = max(mh,m-tp)
    ie = min(mh,tp)
    ml = m-iss+ie
    nl = n*((ml)/m)
    if type(nl) == int:
        nl = nl
    elif nl >= 0:
        nl = int(nl)+1
    else:
        nl = int(nl)
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
def deBoor(k: int, x: int, t, c, p: int):
    """Evaluates S(x).

    Arguments
    ---------
    k: Index of knot interval that contains x.
    x: Position.
    t: Array of knot positions, needs to be padded as described above.
    c: Array of control points.
    p: Degree of B-spline.
    """
    d = [c[j + k - p] for j in range(0, p + 1)]

    for r in range(1, p + 1):
        for j in range(p, r - 1, -1):
            alpha = (x - t[j + k - p]) / (t[j + 1 + k - r] - t[j + k - p])
            d[j] = (1.0 - alpha) * d[j - 1] + alpha * d[j]

    return d[p]
para = [i for i in range(0,31)]
knots = entrega2(para,30,9,3,2,2)
points = entrega22(para,30,9,3,2,2)
print(len(knots), len(points))
p = 3
cant_divisiones = 20
X = []
Y = []
trazadores = []
maxpoints = len(knots) #maxima cantidad de nodos
for rango in range(p,maxpoints-p-1):
    divisiones = np.linspace(knots[rango],knots[rango+1],cant_divisiones)      
    for punto in divisiones:
        result = deBoor(rango, punto, knots, points, p)
        print(result)
        X.append(result[0])
        Y.append(result[1])
plt.plot(points[:,0], points[:,1],'.')
plt.plot(X,Y)
plt.show()