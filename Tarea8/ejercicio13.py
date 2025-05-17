
import requests
import json

def obt_peliculas():
    url_base="https://swapi.py4e.com/api/films/"
    try:
        respuesta=requests.get(url_base)
        respuesta.raise_for_status()
        info=respuesta.json()
        return info["results"]
    except requests.exceptions.RequestException as e:
        print("Hubo un error de conexion/solicitud:", e)
        return list()

def guardar_archivo(peliculas,nom_archivo):
        with open(nom_archivo,"w") as archivo:
            json.dump(peliculas, archivo)

peliculas=obt_peliculas()

peliculas_info=[
    {"titulo": peli["title"], "fecha_lanzamiento": peli["release_date"]}
    for peli in peliculas
]

print("Lista de películas de Star Wars:")
for peli in peliculas_info:
    print(f"{peli['titulo']} (Lanzamiento: {peli['fecha_lanzamiento']})")

guardar_archivo(peliculas_info,"peliculas_star_wars.json")
