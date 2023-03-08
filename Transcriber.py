import requests
import json

def transcribe():
    url = "http://localhost:9000/asr"
    querystring = {"task": "transcribe", "language": "es", "output": "txt"}
    payload = {}
    files = [
    ('audio_file', ('output.wav', open('output.wav', 'rb'), 'audio/wav'))
    ]
    headers = {
    'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files, params=querystring)

    print(response.text)

    response_text = response.text # Guarda la respuesta como texto en una variable

    with open("archivo.txt", "w") as archivo:
        # Escribe el contenido de la variable en el archivo
        archivo.write(response_text)

    # Cierra el archivo
    archivo.close()

transcribe()