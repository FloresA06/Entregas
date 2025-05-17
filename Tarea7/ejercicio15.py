
import re

correo_e=input("Ingresar direccion de correo electronico: ")

f_direccion=re.compile(r"\D+@\D+\.\D{3}")

mail=f_direccion.search(correo_e)
if mail!=None:
    print("Direccion valida")
else:
    print("Direccion invalida")



