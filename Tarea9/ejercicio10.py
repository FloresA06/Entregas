
import matplotlib.pyplot as plt

fig,ax=plt.subplots()

categorias=["A","B","C","D"]
valores=[10,20,15,25]
colores=["red","blue","green","purple"]

ax.set_xlabel("Categorias")
ax.set_ylabel("Valores")
ax.bar(categorias,valores,color=colores)

plt.show()
