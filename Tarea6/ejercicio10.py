
def reg_ventas():
    ventas=list()
    n=int(input("Numero de ventas a registrar: "))
    for i in range(n):
        print(f"\nNumero de venta: {i + 1}")
        producto=input("Nombre del producto: ").strip()
        mes=input("Mes de la venta: ").strip()
        cantidad=int(input("Cantidad vendida: "))
        venta={
            "producto": producto,
            "mes": mes,
            "cantidad_vendida": cantidad
        }
        ventas.append(venta)
    return ventas

def mostrar_ventas(ventas):
    print("\nVentas registradas:")
    for v in ventas:
        print(f"Producto: {v['producto']}\nMes: {v['mes']}\nCantidad Vendida: {v['cantidad_vendida']}")

ventas_registradas = reg_ventas()
mostrar_ventas(ventas_registradas)
