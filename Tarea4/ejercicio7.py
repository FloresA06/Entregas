
import math

def pol_cartesiana(coordenada_polar):
    r,theta_grados=coordenada_polar
    theta_radianes=math.radians(theta_grados)
    x=r*math.cos(theta_radianes)
    y=r*math.sin(theta_radianes)
    return (x,y)

r=float(input("Ingrese el valor del radio: "))
theta=float(input("Ingrese el valor de θ en grados): "))

coordenada_polar=(r, theta)
coordenada_cartesiana=pol_cartesiana(coordenada_polar)

print(f"La coordenada polar: {coordenada_polar}")
print(f"La coordenada cartesiana: {coordenada_cartesiana}")
