
import re

n_usuario=input("Ingresar usuario: ")

pat_valido=re.compile(r"\w{3,16}")

validar_usuario=pat_valido.search(n_usuario)

print(validar_usuario)


"""if validar_usuario!=None:
    print("Nombre de usuario valido")
else:
    print("Nombre de usuario invalido")"""