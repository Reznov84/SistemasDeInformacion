import csv


"""with open('datos.txt', 'r') as archivo:
    contedido = archivo.read()
    print(contedido)"""

"""with open('datos.txt', 'r') as archivo:
    contenido=archivo.readlines()
    for c in contenido:
        print(c)"""

"""ARCHIVO = 'datos.txt'

def escribe(texto):
    with open (ARCHIVO, 'a') as archivo:
        archivo.write(texto + '\n')

        def lectura():
            with open(ARCHIVO, 'r') as archivo:
                contenido = archivo.readlines()
                return contenido


    name = '-'
    while name:
        name = input('Ingresa el nombre: ').capitalize()
        escribe(name)"""

"""def carga_datos():
        try:
            with open("datos.txt", "r") as archivo:
                datos = archivo.readlines()
                return datos 
        except:
            print("hubo un error")    
if __name__ =='__main__':
        datos=carga_datos()
        print(datos)"""

def leer():
    datos= []
    with open("datos.txt", "r") as archivo:
        lector = csv.reader(archivo)
        for row in lector:
            datos.append(row)
    return datos

datos = leer()
"""for dato in datos:"""
print(datos[0]['nombre']) 

            