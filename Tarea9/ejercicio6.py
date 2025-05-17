
import matplotlib.pyplot as plt

fig,ax=plt.subplots()

cat=["A","B","C","D"]
val=[10,20,15,25]

ax.set_xlabel("Categorias")
ax.set_ylabel("Valores")

ax.bar(cat, val, color="blue")
plt.show()
