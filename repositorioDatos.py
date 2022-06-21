import csv

class RepositorioDatos:
  def __init__(self):
    self.nombreArchivoPuntosControl = "datos/datosPrueba/helice.txt"
    self.nombreArchivoNodos = "datos/datosPrueba/nodos3d.txt"
    self.nombreArchivoPuntosQ= "datos/datosPrueba/helice.txt"
    self.nombreArchivoDerIn= "datos/datosPrueba/derIniciales.txt"
    self.nombreArchivoDerFin= "datos/datosPrueba/derFinales.txt"
    return

  def getNombreArchivoPuntosControl(self):
    return self.nombreArchivoPuntosControl

  def getNombreArchivoNodos(self):
    return self.nombreArchivoNodos
  
  def getNombreArchivoPuntosQ(self):
    return self.nombreArchivoPuntosQ

  def getNombreArchivoDerIn(self):
    return self.nombreArchivoDerIn
  
  def getNombreArchivoDerFin(self):
    return self.nombreArchivoDerFin

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

  def obtenerPuntosQ(self):
    try:
      with open(self.nombreArchivoPuntosQ, 'r') as archivo:
        lineas = csv.reader(archivo)
        puntosQ = self.convertirLineasAPuntosQ(lineas)
    except FileNotFoundError:
      print("No se encuentra el archivo con los puntos Q")
      exit()
    return puntosQ
  
  def obtenerDerIn(self):
    try:
      with open(self.nombreArchivoDerIn, 'r') as archivo:
        lineas = csv.reader(archivo)
        derIn = self.convertirLineasAPuntosDerIn(lineas)
    except FileNotFoundError:
      print("No se encuentra el archivo con las derivadas iniciales")
      exit()
    return derIn

  def obtenerDerFin(self):
    try:
      with open(self.nombreArchivoDerFin, 'r') as archivo:
        lineas = csv.reader(archivo)
        derFin = self.convertirLineasAPuntosDerFin(lineas)
    except FileNotFoundError:
      print("No se encuentra el archivo con las derivadas finales")
      exit()
    return derFin

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
      if len(linea)>2:
        try:
          x = float(linea[0])
          y = float(linea[1])
          z = float(linea[2])
          puntos.append([x, y, z])
        except IndexError:
          print("No se encuentran solo tres coordenadas de puntos de control por línea.")
          exit()
        except ValueError:
          print("Los puntos de control deben ser de caracter numérico.")
          exit()
      else:
        try:
          x = float(linea[0])
          y = float(linea[1])
          puntos.append([x, y])
        except IndexError:
          print("No se encuentran solo dos coordenadas de puntos de control por línea.")
          exit()
        except ValueError:
          print("Los puntos de control deben ser de caracter numérico.")
          exit()
    return puntos
 
  def convertirLineasAPuntosQ(self, lineas):
    puntosQ = []
    for linea in lineas:
      if len(linea)>2:
        try:
          x = float(linea[0])
          y = float(linea[1])
          z = float(linea[2])
          puntosQ.append([x, y, z])
        except IndexError:
          print("No se encuentran solo tres coordenadas de puntos Q por línea.")
          exit()
        except ValueError:
          print("Los puntos Q deben ser de caracter numérico.")
          exit()
      else:
        try:
          x = float(linea[0])
          y = float(linea[1])
          puntosQ.append([x, y])
        except IndexError:
          print("No se encuentran solo dos coordenadas de puntos Q por línea.")
          exit()
        except ValueError:
          print("Los puntos Q deben ser de caracter numérico.")
          exit()
    return puntosQ

  def convertirLineasAPuntosDerIn(self, lineas):
    derIn = []
    for linea in lineas:
      if len(linea)>2:
        try:
          x = float(linea[0])
          y = float(linea[1])
          z = float(linea[2])
          derIn.append([x, y, z])
        except IndexError:
          print("No se encuentran solo tres coordenadas de derivada por línea.")
          exit()
        except ValueError:
          print("Las derivadas deben ser de caracter numérico.")
          exit()
      else:
        try:
          x = float(linea[0])
          y = float(linea[1])
          derIn.append([x, y])
        except IndexError:
          print("No se encuentran solo dos coordenadas de derivada por línea.")
          exit()
        except ValueError:
          print("Las derivadas deben ser de caracter numérico.")
          exit()
    return derIn

  def convertirLineasAPuntosDerFin(self, lineas):
    derFin = []
    for linea in lineas:
      if len(linea)>2:
        try:
          x = float(linea[0])
          y = float(linea[1])
          z = float(linea[2])
          derFin.append([x, y, z])
        except IndexError:
          print("No se encuentran solo tres coordenadas de derivada por línea.")
          exit()
        except ValueError:
          print("Las derivadas deben ser de caracter numérico.")
          exit()
      else:
        try:
          x = float(linea[0])
          y = float(linea[1])
          derFin.append([x, y])
        except IndexError:
          print("No se encuentran solo dos coordenadas de derivada por línea.")
          exit()
        except ValueError:
          print("Las derivadas deben ser de caracter numérico.")
          exit()
    return derFin