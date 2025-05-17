
import requests

llave="TU_API_KEY"
ciudad=str(input("Ingrese la ciudad a buscar: "))
c_pais=str(input("codigo del pais (opcional) en mayusculas: "))

url_base="http://api.openweathermap.org/geo/1.0/direct"
params={
    "q": f"{ciudad},{c_pais}",
    "limit": 1,
    "appid": llave
}

try:
    respuesta=requests.get(url_base, params=params)
    respuesta.raise_for_status()
    info=respuesta.json()
    if info:
        ciudad_e=info[0]["name"]
        latitud=info[0]["lat"]
        longitud=info[0]["lon"]
        print(f"Ciudad: {ciudad_e}")
        print(f"Coordenadas: Latitud={latitud}, Longitud={longitud}")
    else:
        print("Ciudad no encontrada")

except requests.exceptions.RequestException as e:
    print("Hubo un error de conexion/solicitud:", e)
except (KeyError, IndexError):
    print("Error al procesar datos")
