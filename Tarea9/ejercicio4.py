
from sympy import *

a=float(input("Ingrese un numero flotante con el que se va a evaluar el limite: "))
x=symbols("x")

expr_b=x**2+3*x+2
funcion=limit(expr_b,x,a)

limite=limit(funcion,x,a)
derivada=diff(funcion,x)

print(f"Límite de f(x) cuando x tiende a {a}: {limite:.3f}")
print(f"Derivada de f(x): {derivada}")
