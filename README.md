# Diseno Geometrico
Proyecto final para Programación Científica.

Implementación del algoritmo de De Boor para evaluar curvas B-Spline. 

En el repositorio se pueden encontrar diferentes archivos, unos correspondientes al código del programa (módulos), y otros referentes a los datos de entrada para la ejecución de ellos. Para el correcto funcionamiento del programa realizado, es necesario que el usuario se dirija a la carpeta "datos" y en el archivo "nodos.txt" ingrese los nodos con los que se desee trabajar, uno por línea. El usuario también debe proveer un archivo de texto "puntosControl.txt" se deben escribir los puntos de control para la curva en el formato

x1, y1
x2, y2

Nota: Recuerde que en caso de que no se ingresen los valores adecuados, el programa arrojará un mensaje de error.
Aparte, se encuentra un archivo llamado "Boor" donde se encuentra la clase que permite desarrollar el algoritmo de Boor a partir de los archivos de texto de entrada, y otro denominado "repositorioDatos" que desarrolla todo el manejo de errores (Error Handling) para que el programa se pueda ejecutar de la manera adecuada, y no interprete caracteres de forma no deseada. Finalmente, en el archivo "pruebasBoor" se importan los módulos anteriormente mencionados para poder ejecutar el algoritmo de Boor para las curvas B-Spline a partir de los datos ingresados en los archivos de la carpeta "datos", y que se haga el correspondiente manejo y excepción de errores. Finalmente, este último documento realiza una gráfica donde se puede apreciar la curva B-Spline en su máximo esplendor, así como el polígono de control correspondiente. Cabe aclarar que la gráfica está diseñada para recibir dos coordenadas para hacer la curva en dos dimensiones, sin embargo, es posible usar el programa para tres coordenadas, e ilustrar los resultados en tres dimensiones.

Implementación del algoritmo descrito en "Least-squares B-spline curve approximation with arbitrary end derivatives" (Engineering with Computers, 16(2), pp. 109-116.) para aproximar una curva B-Spline a un conjunto de observaciones.
