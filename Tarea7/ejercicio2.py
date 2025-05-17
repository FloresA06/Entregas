
with open("nombres.txt","r") as archivo: 
    contenido=archivo.read()

nombres=contenido.split()
print(nombres)
