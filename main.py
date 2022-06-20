import os 

ver = 0
while ver==0:
    a = input("1: Curva B-spline con Puntos de Control y Nodos por archivo\n2: Curva B-spline por aproximación de mínimos cuadrados\n3: Curva B-spline interactiva\n")
    try:
        a= int(a)
        ver=1
    except:
        print("Por favor escoger una opción por medio de un valor numérico entre 1, 2 y 3\n")

if a==1:
    os.system('python pruebasBoorConPCyNDados.py')
elif a==2:
    os.system('python aproxMinCuadrados.py')
elif a==3:
    os.system('python Interactivo.py')
else:
    print("No está dentro de las opciones")
