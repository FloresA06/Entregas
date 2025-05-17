
import re

texto=input("Ingresar texto a leer: ")
for_tel=re.compile(r"\+\d{2}(\s|\-)\d{4}(\s|\-)\d{4}")

enc_tel=re.findall(for_tel, texto)
print(f"Se econtraron como coincidencias a: {enc_tel}")