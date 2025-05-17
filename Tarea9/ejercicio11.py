
import matplotlib.pyplot as plt
import numpy as np

fig,ax=plt.subplots()

x=[1,2,3,4,5]
y=[2,3,5,7,11]
tamaños=[20,50,80,100,150]
colores = np.random.uniform(15, 80, len(x))

ax.scatter(x, y, s=tamaños, c=colores, vmin=0, vmax=100)
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")

plt.show()
