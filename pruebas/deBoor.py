def calcularPuntoEnIntervalo(i: int, x: int, nodos, c, grado: int):
    """Evaluates S(x).

    Arguments
    ---------
    i: Index of knot interval that contains x.
    x: Position.
    nodos: Array of knot positions, needs to be padded as described above.
    c: Array of control points.
    grado: Degree of B-spline.
    """
    d = [c[j + i - grado] for j in range(0, grado + 1)]

    for r in range(1, grado + 1):
        for j in range(grado, r - 1, -1):
            alpha = (x - nodos[j + i - grado]) / (nodos[j + 1 + i - r] - nodos[j + i - grado])
            d[j] = (1.0 - alpha) * d[j - 1] + alpha * d[j]

    return d[grado]