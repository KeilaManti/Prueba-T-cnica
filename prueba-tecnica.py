import os

def buscarPalabra(archivo, palabra):
    cantidad = 0
    archivoLeido = open(archivo, encoding="utf8")
    lineasArchivo = []
    if os.stat(archivo).st_size == 0:
        print("El archivo esta vacio")
    for linea in archivoLeido:
        linea = linea[0:-1]
        c = linea.count(palabra)
        cantidad=cantidad+c
        if c > 0:
            lineasArchivo.append(linea)
    archivoLeido.close()
    return [cantidad, lineasArchivo]

palabra = "dragones"
archivo = "La comunidad del anillo.txt"
resultado = buscarPalabra(archivo, palabra)
print("La cantidad de veces que aparece la palabra", palabra, "es :", resultado[0], "\n")
print("Las lineas donde aparecio la palabra son:")

for linea in resultado[1]:
    print(linea)

