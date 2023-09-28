import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas_cafeteria.csv")

trends = df.groupby("Producto")["Cantidad"].sum()

plt.bar(trends.index, trends.values)
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.title("Sales Trends")
plt.xticks(rotation=45)
plt.show()
