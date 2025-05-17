
import requests

def obtener_planetas():
    url="https://swapi.py4e.com/api/planets/"
    planetas=list()
    try:
        while url:
            respuesta=requests.get(url)
            respuesta.raise_for_status()
            data=respuesta.json()
            planetas.extend(data['results'])
            url=data['next']
    except requests.exceptions.RequestException as e:
        print("Hubo un error de conexion:", e)
        return list()
    return planetas

def prom_poblacion(planetas):
    poblaciones=list()
    for planeta in planetas:
        poblacion=planeta['population']
        if poblacion.isdigit():
            poblaciones.append(int(poblacion))
    if poblaciones:
        promedio=sum(poblaciones)/len(poblaciones)
        return promedio
    else:
        return None

planetas=obtener_planetas()
if planetas:
    promedio=prom_poblacion(planetas)
    if promedio is not None:
        print(f"El promedio de poblacion de los planetas es: {int(promedio):,}")
    else:
        print("No es posible calcular el promedio")
else:
    print("No fue posible obtener la lista de planetas")
