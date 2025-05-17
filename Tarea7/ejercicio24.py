
import re

texto=input("Ingresar texto a buscar: ")

for_decimal=re.compile(r"((\s*|\-)\d*\.\d+)|((\s*|\-)\d*\,\d+)")
print(f"Se econtraron como coincidencias: {for_decimal.findall(texto)}")