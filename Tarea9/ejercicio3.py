
import random
from statistics import median, mean, mode
datos=list()

for x in range(25):
    num=random.randint(0,50)
    datos.append(num)

print(f"teniendo los el conjunto de datos: {datos}")
print(f"media= {mean(datos)}\nmediana= {median(datos)}\nmoda= {mode(datos)}")
