import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ventas_cafeteria.csv")

trends = df.groupby("Producto")["Cantidad"].sum()

plt.bar(trends.index, trends.values)
plt.xlabel("Producto")
plt.ylabel("Cantidad")
plt.title("Sales Trends")

best_selling = trends.idxmax()
least_selling = trends.idxmin()

print(f"La bebida mejor vendida fue: {best_selling}")
print(f"La bebida peor vendida fue: {least_selling}")

plt.xticks(rotation=45)
plt.show()
