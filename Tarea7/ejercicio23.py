
import re

texto=input("Ingrese el texto a buscar: ")

iso_8601=re.compile(r"\d{4}\-[0-1][0-9]\-[0-3][0-9]")
print(iso_8601.findall(texto))