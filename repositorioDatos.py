import csv

class RepositorioDatos:
  def __init__(self):
    self.nombreArchivoPuntosControl = "datos/puntosControl2.txt"
    self.nombreArchivoNodos = "datos/nodos.txt"
    return

  def getNombreArchivoPuntosControl(self):
    return self.nombreArchivoPuntosControl
  
  def getNombreArchivoNodos(self):
    return self.nombreArchivoNodos
  
  def obtenerPuntosControl(self):
    try:
      with open(self.nombreArchivoPuntosControl, 'r') as archivo:
        lineas = csv.reader(archivo)
        puntosControl = self.convertirLineasAPuntos(lineas)
    except FileNotFoundError:
      print("No se encuentra el archivo con los puntos de control.")
      exit()
    return puntosControl
  
  def obtenerNodos(self):
    try:
      with open(self.nombreArchivoNodos, 'r') as archivo:
        lineas = csv.reader(archivo)
        knots = self.convertirLineasALista(lineas)
    except FileNotFoundError:
      print("No se encuentra el archivo con los nodos.")
      exit()
    return knots

  def convertirLineasALista(self, lineas):
    lista = []
    for linea in lineas:
      try:
        lista.append(float(linea[0]))
      except ValueError:
        print("Los nodos deben ser únicos y de caracter numérico.")
        exit()
    return lista
  
  def convertirLineasAPuntos(self, lineas):
    puntos = []
    for linea in lineas:
        try:
          x = float(linea[0])
          y = float(linea[1])
          puntos.append([x, y])
        except IndexError:
          print("No se encuentran solo dos puntos de control por línea.")
          exit()
        except ValueError:
          print("Los puntos de control deben ser de caracter numérico.")
          exit()
    return puntos


