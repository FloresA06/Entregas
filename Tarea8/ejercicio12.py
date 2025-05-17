
import requests
import time
from datetime import datetime, timedelta

llave="939b89667c1e6fd0423d4063a5f854b0"
latitud=float(input("Ingrese la latitud del pais: "))
longitud=float(input("Ingrese la longitud del pais: "))
url_base="https://api.openweathermap.org/data/3.0/onecall/timemachine"

def temp_promedio(timestamp):
    params={
        "lat": latitud,
        "lon": longitud,
        "dt": timestamp,
        "appid": llave,
        "units": "metric"
    }
    try:
        respuesta=requests.get(url_base, params=params)
        respuesta.raise_for_status()
        info=respuesta.json()
        temps=[hour["temp"] for hour in info.get("hourly", [])]
        if temps:
            return sum(temps)/len(temps)
        else:
            print("Faltan datos de temperatura para una fecha")
            return None
    except requests.exceptions.RequestException as e:
        print("Hubo un error de conexion/solicitud:",e)
        return None

print("Temperatura promedio diaria de una semana:\n")
for i in range(1,8):
    fecha=datetime.utcnow() - timedelta(days=i)
    timestamp=int(fecha.timestamp())

    promedio=temp_promedio(timestamp)
    if promedio is not None:
        print(f"{fecha.strftime('%Y-%m-%d')}: {promedio:.2f} °C")
