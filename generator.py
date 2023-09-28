import random
import pandas as pd
from datetime import datetime, timedelta

menu = {
    "Capuchino": {"Chico": 40, "Mediano": 50, "Grande": 60},
    "Moka": {"Chico": 40, "Mediano": 50, "Grande": 60},
    "Americano": {"Chico": 30, "Mediano": 40, "Grande": 50},
    "Chai": {"Chico": 40, "Mediano": 50, "Grande": 60},
    "Frapuchino": {"Chico": 50, "Mediano": 60, "Grande": 70}
}

def generar_venta():
    producto = random.choice(list(menu.keys()))
    tamaño = random.choice(list(menu[producto].keys()))
    precio = menu[producto][tamaño]
    cantidad = random.randint(1, 3)
    fecha = datetime(2023, 9, 25) + timedelta(days=random.randint(0, 7))
    return {"Producto": producto, "Tamaño": tamaño, "Precio": precio, "Cantidad": cantidad, "Fecha": fecha}

n = int(input("Ingrese el número de ventas imaginarias a generar: "))

ventas = [generar_venta() for _ in range(n)]

df = pd.DataFrame(ventas)

df.to_csv("ventas_cafeteria.csv", index=False)

print(f"Se han generado y guardado {n} ventas en el archivo 'ventas_cafeteria.csv'.")

