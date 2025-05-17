
import requests

def naves_o():
    url_base="https://swapi.dev/api/starships/"
    naves=list()
    try:
        while url_base:
            response=requests.get(url_base)
            response.raise_for_status()
            info=response.json()
            naves.extend(info["results"])
            url_base=info["next"]
    except requests.exceptions.RequestException as e:
        print("Hubo un error de conexion:", e)
        return list()
    return naves

def filtrar_cap(naves, comp=100000):
    naves_filtradas=list()
    for nave in naves:
        carga=nave.get("cargo_capacity","unknown")
        if carga.isdigit() and int(carga)>comp:
            naves_filtradas.append({
                "nombre": nave["name"],
                "modelo": nave["model"],
                "carga": int(carga)
            })
    return naves_filtradas

naves=naves_o()
naves_filtradas=filtrar_cap(naves, 100000)

print("Las naves con capacidad de carga mayor a 100,000 son:")
for nave in naves_filtradas:
    print(f"{nave['nombre']} (Modelo: {nave['modelo']}, Carga: {nave['carga']})")
