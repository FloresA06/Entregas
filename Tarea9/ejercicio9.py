
import matplotlib.pyplot as plt

x=[0,1,2,3,4,5]
y1=[0,1,4,9,16,25]
y2=[0,1,2,3,4,5]

plt.plot(x, y1, color="blue", linestyle="dotted")
plt.plot(x, y2, color="red", linestyle="dashdot") 

plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.show()
