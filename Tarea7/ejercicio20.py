
import re

num_tarjeta=input("Numero de tarjeta: ")

formato_t=re.compile(r"(\d{4}\-){3}\d{4}")
val_numt=formato_t.search(num_tarjeta)

if val_numt!=None:
    print("Numero valido")
else:
    print("Numero invalido")