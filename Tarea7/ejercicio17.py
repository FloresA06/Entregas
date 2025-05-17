
import re

fecha=input("Ingresar fecha con el formato DD/MM/AAAA: ")
formato_f=re.compile(r"[0-3][0-9]/[0-1][0-9]/\d{4}")

val_fecha=formato_f.search(fecha)
print(val_fecha)

if val_fecha!=None:
    print("Formato de fecha es valido")
else:
    print("Formato de fecha es invalido")