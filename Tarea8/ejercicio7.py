
import requests

def obtener_personajes(start=1, end=10):
    url_base="https://swapi.py4e.com/api/people/"
    personajes=list()
    for i in range(start, end + 1):
        resp=requests.get(f"{url_base}{i}/")
        if resp.status_code==200:
            data=resp.json()
            personajes.append({
                "nombre": data.get("name"),
                "altura": data.get("height")
            })
        else:
            print(f"No se pudo obtener el personaje con ID {i}")
    return personajes

def filtrar_personajes(personajes, letra="L"):
    return [per for per in personajes if per["nombre"].startswith(letra)]

characters=obtener_personajes(1, 10)
filtrado=filtrar_personajes(characters,"L")
print("Personajes cuyo nombre comienza con 'L' y su altura:")
for per in filtrado:
    print(f"{per['nombre']}: {per['altura']} cm")
