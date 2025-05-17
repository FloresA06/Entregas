
import matplotlib.pyplot as plt

categorias=["A","B","C","D"]
valores=[10,20,15,25]

fig, ax = plt.subplots()
grafica=ax.bar(categorias, valores, color="crimson")
ax.set(ylabel="Valores",xlabel="Categorias", ylim=(0, 30))
ax.bar_label(grafica, fmt='{:,.0f}')

plt.show()
