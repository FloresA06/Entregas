
import requests

api_key="Apikey"
url_base="https://api.openweathermap.org/data/2.5/weather"

ciudad=str(input("Ingrese la ciudad a cosultar: "))

params = {
    "q": ciudad,
    "appid": api_key,
    "units": "metric",
    "lang": "es"
}
try:
    respuesta=requests.get(url_base,params=params)
    info=respuesta.json()
    temperatura=info["main"]["temp"]
    humedad=info["main"]["humidity"]
    descripcion=info["weather"][0]["description"]
    print(f"Clima en {ciudad}:")
    print(f"Temperatura: {temperatura} °C")
    print(f"Humedad: {humedad}%")
    print(f"Descripcion: {descripcion.capitalize()}")
except requests.exceptions.HTTPError as http_err:
    if respuesta.status_code == 404:
        print("La ciudad no encontrada")
    else:
        print(f"Error HTTP: {http_err}")
except requests.exceptions.RequestException:
    print("Error de conexión")
