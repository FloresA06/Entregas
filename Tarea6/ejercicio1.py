
def dic_precios():
    productos=dict()
    n=int(input("Numero de productos a ingresa: "))
    for i in range(n):
        prod=input(f"Ingrese el nombre del producto: ").strip().lower()
        precio=float(input(f"Ingrese el precio del producto: "))
        productos[prod]=precio
    return productos

def buscar_precio(productos):
    prod=input("\nIngrese el nombre del producto a buscar: ").strip().lower()
    if prod in productos:
        print(f"El precio de {prod} es: ${productos[prod]:.2f}")
    else:
        print(f"El producto {prod} no está registrado.")

diccionario=dic_precios()
buscar_precio(diccionario)
