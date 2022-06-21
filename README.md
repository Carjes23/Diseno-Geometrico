# Diseno Geometrico
Proyecto final para Programación Científica.

Este repositorio se compone principalmente de tres partes, la primera, por medio de unos puntos de control y nodos dados por el usuario por medio de un archivo de texto, se crea una curva B-Spline a través del algoritmo de De Boor. 
En la segunda parte, se tiene la aproximación por medio de mínimos cuadrados, donde luego de ingresar ciertos datos se optienen los puntos de control y nodos óptimos para la aproximación B-Spline.
En la tercera parte, se propone una implementación interactiva, que permite experimentar al poner puntos aleatorios la creación de curvas B-Spline. 

Se propone como método de ejecución el archivo main.py, en el cual se escoge la opción entre las partes deseada.

Para la ejecución de la primera parte es necesario que el usuario se dirija a la carpeta "datos" y en el archivo "nodos.txt" ingrese los nodos con los que se desee trabajar, uno por línea. El usuario también debe proveer un archivo de texto "puntosControl.txt" se deben escribir los puntos de control para la curva en el formato:
x1, y1
x2, y2
Además, al momento de ejecutarse se solicitará el grado de la curva B-Spline.

Para la ejecución de la segunda parte, en la misma carpeta de datos se requiere modificar el archivo "puntosQ.txt", con los datos deseados, el cual tiene el mismo formato anteriormente mencionado para los puntos de control. Además, se solicitara el grado del B-Spline y el número de puntos de control deseados. 

Para la última parte, se requiere el grado del B-Spline y el número de puntos de control. También, que al escoger los puntos interactivamente estos sean mayores a los puntos de control. Con click izquierdo se escogen los puntos y con click derecho se remueven, además se pueden arrastrar de ser necesario.

Nota: Recuerde que en caso de que no se ingresen los valores adecuados, el programa arrojará un mensaje de error.
Aparte, se encuentra un archivo llamado "Boor" donde se encuentra la clase que permite desarrollar el algoritmo de Boor a partir de los archivos de texto de entrada, y otro denominado "repositorioDatos" que desarrolla todo el manejo de errores (Error Handling) para que el programa se pueda ejecutar de la manera adecuada, y no interprete caracteres de forma no deseada. Finalmente, en el archivo "pruebasBoor" se importan los módulos anteriormente mencionados para poder ejecutar el algoritmo de Boor para las curvas B-Spline a partir de los datos ingresados en los archivos de la carpeta "datos", y que se haga el correspondiente manejo y excepción de errores. Finalmente, este último documento realiza una gráfica donde se puede apreciar la curva B-Spline en su máximo esplendor, así como el polígono de control correspondiente. Cabe aclarar que la gráfica está diseñada para recibir dos coordenadas para hacer la curva en dos dimensiones, sin embargo, es posible usar el programa para tres coordenadas, e ilustrar los resultados en tres dimensiones.

Implementación del algoritmo descrito en "Least-squares B-spline curve approximation with arbitrary end derivatives" (Engineering with Computers, 16(2), pp. 109-116.) para aproximar una curva B-Spline a un conjunto de observaciones.
