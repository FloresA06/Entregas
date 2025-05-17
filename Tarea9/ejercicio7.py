
import matplotlib.pyplot as plt

fig, ax=plt.subplots()

cat=["A","B","C","D"]
val=[10,20,15,25]

ax.set_xlabel("Valores")
ax.set_ylabel("Categorias")

ax.barh(cat,val,color="green")
plt.show()
