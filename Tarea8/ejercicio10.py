
import requests
import json
from collections import defaultdict
from datetime import datetime

llave="939b89667c1e6fd0423d4063a5f854b0"
ciudad=str(input("Cuidad a buscar: "))
url_base="https://api.openweathermap.org/data/2.5/forecast"

params = {
    "q": ciudad,
    "appid": llave,
    "units": "metric",
    "lang": "es"
}

try:
    respuesta=requests.get(url_base,params=params)
    respuesta.raise_for_status()
    info=respuesta.json()
    temps_diarias=defaultdict(list)
    for entry in info["list"]:
        dt_txt=entry["dt_txt"]
        fecha_str=dt_txt.split(" ")[0]
        temp=entry["main"]["temp"]
        temps_diarias[fecha_str].append(temp)
    forecast=list()
    for date,temps in temps_diarias.items():
        min_temp=min(temps)
        max_temp=max(temps)
        forecast.append({
            "fecha": date,
            "temperatura_minima": min_temp,
            "temperatura_maxima": max_temp
        })
    print(f"Pronostico para {ciudad} en la proxima semana:")
    for dia in forecast[:5]:
        print(f"{dia['fecha']}: Minimo {dia['temperatura_minima']}°C | Maximo {dia['temperatura_maxima']}°C")

    with open("pronostico_5.json","w",encoding="utf-8") as archivo:
        json.dump(forecast[:5],archivo,ensure_ascii=False)

except requests.exceptions.HTTPError as err:
    print("Error en la solicitud:",err)
except requests.exceptions.RequestException:
    print("Error de conexion")
except KeyError:
    print("Error al procesar los datos")
