import csv

#cargar el inventario 
inventario = {}
with open("inventario.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Saltar la primera fila
    for row in csv_reader:
        producto, cantidad = row
        inventario[producto] = int(cantidad)

#recetas de cafe
recetas = {
    "Cafe Americano": {"Agua": 500, "Cafe": 10, "Vasos": 1},
    "Cafe Latte": {"Agua": 300, "Leche": 200, "Cafe": 15, "Vasos": 1},
    "Cafe Espresso": {"Agua": 100, "Cafe": 15, "Vasos": 1},
}

#quitar ingredientes del inventario
def sustraer_ingredientes(receta, cantidad):
    for ingrediente, cantidad_necesaria in recetas[receta].items():
        inventario[ingrediente] -= cantidad_necesaria * cantidad

#verificar si hay suficientes ingredientes
def verificar_disponibilidad(receta, cantidad):
    for ingrediente, cantidad_necesaria in recetas[receta].items():
        if inventario[ingrediente] < cantidad_necesaria * cantidad:
            return False
    return True

#mostrar el inventario
def mostrar_inventario():
    print("Inventario:")
    for producto, cantidad in inventario.items():
        print(f"{producto}: {cantidad}")

#menu para el usuario
while True:
    print("\nMenú de Cafetería:")
    for cafe in recetas:
        print(f"- {cafe}")
    print("0 - Salir")

    opcion = input("Elige un café (o 0 para salir): ")
    if opcion == '0':
        break

    if opcion in recetas:
        cantidad = int(input(f"Cantidad de '{opcion}' a preparar: "))
        if verificar_disponibilidad(opcion, cantidad):
            sustraer_ingredientes(opcion, cantidad)
            print(f"Preparando {cantidad} '{opcion}'...")
            print(f"{cantidad} '{opcion}' preparado con éxito.")
        else:
            print("No hay suficientes ingredientes para preparar el café.")
    else:
        print("Café no válido. Por favor, elige una opción válida.")

#guardar los cambios en el inventario
with open("inventario.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Producto", "Cantidad"])
    for producto, cantidad in inventario.items():
        csv_writer.writerow([producto, cantidad])

#mostrar el inventario actualizado
mostrar_inventario()
