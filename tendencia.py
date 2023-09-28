import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas_cafeteria.csv")

trends = df.groupby("Producto")["Cantidad"].sum()

plt.bar(trends.index, trends.values)
plt.xlabel("Producto")
plt.ylabel("Cantidad")
plt.title("Ventas")
plt.xticks(rotation=45)
plt.show()
