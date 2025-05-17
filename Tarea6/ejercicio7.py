
def reg_compras():
    compras=list()
    n=int(input("\nNumero de productos a registrar: "))
    for i in range(n):
        prod=input(f"Nombre del producto #{i + 1}: ").strip()
        cantidad=int(input("Cantidad comprada: "))
        precio_u=float(input("Precio unitario: $"))
        compras.append((prod,cantidad,precio_u))
    return compras

def calcular_total(compras):
    total=0
    for prod,cantidad,precio_u in compras:
        total+=cantidad*precio_u
    return total

def print_compras(compras):
    print("\Total compras:")
    for prod, cantidad,precio_u in compras:
        sub_t=cantidad*precio_u
        print(f"Cantidad {prod}: {cantidad}\Precio unitario: ${precio_u:.2f}\nSubtotal: ${sub_t:.2f}")

u_compras=reg_compras()
print_compras(u_compras)

total = calcular_total(u_compras)
print(f"\nTotal gastado: ${total:.2f}")
