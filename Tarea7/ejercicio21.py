
import re

c_postal=input("Ingrese un codigo postal: ")

pat_val=re.search(r"((\d{5})|(\d{5}\-\d{4}))", c_postal)
if pat_val!=None:
    print("Formato de codigo postal valido")
else:
    print("Formato de codigo postal invalido")