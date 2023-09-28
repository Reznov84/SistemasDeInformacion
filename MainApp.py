cafes = {}
compras ={}
#agregar
def agregar_cafe():
    nombre = input("Ingrese el nombre del café: ")
    if nombre in cafes:
        print(f"El café '{nombre}' ya existe en la lista.")
        return
    descripcion = input("Ingrese la descripción del café: ")
    precio_chico = float(input("Ingrese el precio del café tamaño chico: "))
    precio_mediano = float(input("Ingrese el precio del café tamaño mediano: "))
    precio_grande = float(input("Ingrese el precio del café tamaño grande: "))
    
    cafes[nombre] = {
        'descripcion': descripcion,
        'precios': {
            'chico': precio_chico,
            'mediano': precio_mediano,
            'grande': precio_grande
        }
    }
    print(f"Café '{nombre}' agregado con éxito!")
#listar
def listar_cafes():
    if not cafes:
        print("No hay cafés disponibles.")
    else:
        print("\nLista de cafés disponibles:")
        for nombre, cafe in cafes.items():
            print(f"Nombre: {nombre}")
            print(f"Descripción: {cafe['descripcion']}")
            print("Precios:")
            for tamaño, precio in cafe['precios'].items():
                print(f"{tamaño.capitalize()}: ${precio}")
            print("---------------------------")

#actualizar
def actualizar_cafe():
    nombre = input("Ingrese el nombre del café que desea actualizar: ")
    if nombre in cafes:
        print(f"Café actual: {nombre}")
        print(f"Descripción actual: {cafes[nombre]['descripcion']}")
        print("Precios actuales:")
        for tamaño, precio in cafes[nombre]['precios'].items():
            print(f"{tamaño.capitalize()}: ${precio}")
        
        nueva_descripcion = input("Ingrese la nueva descripción (deje en blanco si no desea cambiar): ")
        nuevos_precios = {}
        
        for tamaño in ['chico', 'mediano', 'grande']:
            precio = input(f"Ingrese el nuevo precio para el tamaño {tamaño} (deje en blanco si no desea cambiar): ")
            if precio:
                nuevos_precios[tamaño] = float(precio)
            else:
                nuevos_precios[tamaño] = cafes[nombre]['precios'][tamaño]
        
        cafes[nombre]['descripcion'] = nueva_descripcion
        cafes[nombre]['precios'] = nuevos_precios
        
        print(f"Café '{nombre}' actualizado con éxito!")
    else:
        print(f"El café '{nombre}' no existe en la lista.")
#eliminar
def eliminar_cafe():
    nombre = input("Ingrese el nombre del café que desea eliminar: ")
    if nombre in cafes:
        del cafes[nombre]
        print(f"Café '{nombre}' eliminado con éxito!")
    else:
        print(f"El café '{nombre}' no existe en la lista.")

        #compra
def realizar_compra():
    listar_cafes()
    if not cafes:
        print("No hay cafés disponibles para comprar.")
        return
    
    nombre = input("Ingrese el nombre del café que desea comprar: ")
    if nombre in cafes:
        tamaño = input("Seleccione el tamaño (chico, mediano o grande): ").lower()
        if tamaño in ['chico', 'mediano', 'grande']:
            cantidad = int(input("Ingrese la cantidad que desea comprar: "))
            if nombre not in compras:
                compras[nombre] = {
                    'descripcion': cafes[nombre]['descripcion'],
                    'precios': {
                        tamaño: cafes[nombre]['precios'][tamaño] * cantidad
                    }
                }
            else:
                if tamaño in compras[nombre]['precios']:
                    compras[nombre]['precios'][tamaño] += cafes[nombre]['precios'][tamaño] * cantidad
                else:
                    compras[nombre]['precios'][tamaño] = cafes[nombre]['precios'][tamaño] * cantidad
            print(f"Compra de '{cantidad}' café(s) '{nombre}' tamaño '{tamaño}' realizada con éxito!")
        else:
            print("Tamaño no válido. Intente de nuevo.")
    else:
        print(f"El café '{nombre}' no existe en la lista.")

# tiquet
def generar_ticket():
    if not compras:
        print("No hay compras para generar el ticket.")
        return
    
    total = 0
    print("\n** Ticket de Compra **")
    for nombre, compra in compras.items():
        cantidad_total = sum(compra['precios'].values()) / min(compra['precios'].values())
        print(f"Nombre: {nombre}")
        print(f"Descripción: {compra['descripcion']}")
        print(f"Cantidad: {int(cantidad_total)}")
        print("Detalle de Precios:")
        for tamaño, precio in compra['precios'].items():
            print(f"Tamaño {tamaño.capitalize()}: ${precio}")
            total += precio
        print("---------------------------")
    print(f"Total a pagar: ${total}")
    print("** Fin del Ticket **")


#menu
while True:
    print("\nMenú Principal:")
    print("1. Agregar Café")
    print("2. Listar Cafés")
    print("3. Actualizar Café")
    print("4. Eliminar Café")
    print("6. Realizar compra")
    print("7. Generar ticket")
    print("8. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        agregar_cafe()
    elif opcion == '2':
        listar_cafes()
    elif opcion == '3':
        actualizar_cafe()
    elif opcion == '4':
        eliminar_cafe()
    elif opcion == '6':
        realizar_compra()
    elif opcion == '7':
        generar_ticket()
    elif opcion == '8':
        break
    else:
        print("Opción no válida. Intente de nuevo.")

       
       