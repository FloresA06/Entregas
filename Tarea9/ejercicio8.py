
import matplotlib.pyplot as plt

etiquetas=["manzanas","naranjas", "platanos", "uvas"]
tamaños=[30,25,20,25]

fig,ax=plt.subplots()
ax.pie(tamaños,labels=etiquetas,colors=["firebrick","orangered","gold","yellowgreen"])

plt.legend(etiquetas)
plt.show()
