import csv
from time import sleep

def register(bebida):
    with open("dataset_ingreso.csv", "a", newline='') as archivo:
        campos = ['bebida', 'descripcion', 'preciochico', 'preciomediano', 'preciogrande']
        escritor = csv.DictWriter(archivo, campos)

        escritor.rwiteheader()
        escritor.writerow({'Nombre': 'Espreso'})

        def primeros precios():
         p1 = random.randint(40, 60)
         p2 = p1 * 1.4
         p3 = p2 * 1.2

