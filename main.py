from flask import Flask
import requests
import json

app = Flask (__name__)

@app.route ("/")
def llamadaAPI ():
    # URL de la API.
    url = "https://hargrimm-wikihow-v1.p.rapidapi.com/steps"

    # Numero de pasos a obtener.
    querystring = {"count":"5"}

    # Headers de la peticion.
    headers = {
        "X-RapidAPI-Key": "8070df0992msh7d97d032e4f12fdp15a65bjsnbe724bdba2ea",
        "X-RapidAPI-Host": "hargrimm-wikihow-v1.p.rapidapi.com"
    }

    # Peticion a la API.
    response = requests.request("GET", url, headers=headers, params=querystring)
    respuestaJSON = response.text

    # Formateamos el JSON a un diccionario de Python.
    datos = json.loads (respuestaJSON)

    return f"<div align='left'><h1>Cinco pasos aleatorios de tutoriales de WikiHow</h1><br><ol><li>{datos['1']}</li><li>{datos['2']}</li><li>{datos['3']}</li><li>{datos['4']}</li><li>{datos['5']}</li></ol></div>"

if __name__ == "__main__":
    app.run ()
