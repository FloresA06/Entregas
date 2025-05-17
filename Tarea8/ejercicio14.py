
import requests

llave="939b89667c1e6fd0423d4063a5f854b0"
latitud=float(input("Ingrese la latitud del pais: "))
longitud=float(input("Ingrese la longitud del pais: "))

url_base="http://api.openweathermap.org/data/2.5/air_pollution"

params={
    "lat": latitud,
    "lon": longitud,
    "appid": llave
}
descripciones_aqi={
    1: "Bueno",
    2: "Moderado",
    3: "Poco saludable para grupos sensibles",
    4: "Poco saludable",
    5: "Muy poco saludable"
}

try:
    respuesta=requests.get(url_base, params=params)
    respuesta.raise_for_status()
    info=respuesta.json()
    aqi=info["list"][0]["main"]["aqi"]
    descripcion=descripciones_aqi.get(aqi, "Desconocido")
    print(f"Indice de calidad del aire: {aqi}")
    print(f"Descripcion: {descripcion}")
except requests.exceptions.RequestException as e:
    print("Hubo un error de conexion/solicitud:", e)
except (KeyError, IndexError):
    print("Error al procesar la respuesta")
