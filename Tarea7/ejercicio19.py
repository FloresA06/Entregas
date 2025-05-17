
import re

texto=input("Ingrese un parrafo de texto: ")

e_mayus=re.findall(r'\b[A-Z]+(?:\s+[A-Z]+)*', texto)

print(e_mayus)