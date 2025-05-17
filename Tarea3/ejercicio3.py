
x = float(input("Ingrese el primer numero: "))
y = float(input("Ingrese el segundo numero: "))

prod = lambda x, y: x * y
mensj=f"El producto de {x} y {y} es:"
print(mensj,prod(x, y))
