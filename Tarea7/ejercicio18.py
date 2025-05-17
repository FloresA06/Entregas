
import re

dir_ipv4=re.compile(r"([0-2][0-5][0-5]\.){3}([0-2][0-5][0-5])")
direccion=input("Direccion ip: ")

val_dir=dir_ipv4.search(direccion)
if val_dir!=None:
    print("Direccion valida")
else:
    print("Direccion invalida")