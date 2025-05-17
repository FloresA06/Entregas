
def dist_e(p1,p2):
    p1=x1,y1
    p2=x2,y2
    distancia=((x2-x1)**2+(y2-y1)**2)**0.5
    return distancia

x1=int(input("Ingrese el primer digito de la primera tupla:"))
y1=int(input("Ingrese el segundo digito de la primera tupla:"))
x2=int(input("Ingrese el primer digito de la segunda tupla:"))
y2=int(input("Ingrese el segundo digito de la segunda tupla:"))

p1=(x1,y1)
p2=(x2,y2)
dist=dist_e(p1,p2)

print(f"Distancia entre {p1} y {p2}: {dist}")
