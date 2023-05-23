from flask import Flask, request, send_file
from Utility import Recorder
from Utility import Transcriber
from Utility import Translator
from Utility import VoiceSpeaker
from pyngrok import ngrok
import atexit
#from EmailSender import sendEmail

#docker voicevox: docker run --rm --gpus all -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
#ngrok http 50021
#127.0.0.1:50021

app = Flask(__name__)
URL = "http://127.0.0.1:50021"

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    # Verificar que se envió un archivo de audio
    if 'audio' not in request.files:
        return 'No se encontró archivo de audio', 400

    audio_file = request.files['audio']

    # Guardar el archivo en el sistema de archivos
    audio_file.save('.\\AudioSources\\mobileFile.mp3')

    return 'Archivo de audio guardado correctamente', 200

@app.route('/return_audio', methods=['GET'])
def return_audio():
    transcription = Transcriber.transcribe(".\\AudioSources\\mobileFile.mp3")
    JAtranslation = Translator.translate(transcription, "JA")
    VoiceSpeaker.speak(JAtranslation, URL, False)
    return send_file(".\\AudioSources\\audio.wav", as_attachment=True)

http_tunnel = ngrok.connect(5000, "http")
http_docker_tunnel = ngrok.connect(50021, "http")

print("------------------------------------------------------")
print("URL del túnel HTTP de Flask:", http_tunnel.public_url)
print("URL del túnel HTTP de Docker:", http_docker_tunnel.public_url)
print("------------------------------------------------------")

def shutdown():
    ngrok.disconnect(http_tunnel.public_url)
    ngrok.disconnect(http_docker_tunnel.public_url)
    ngrok.kill()
atexit.register(shutdown)

if __name__ == '__main__':
    app.run(host='0.0.0.0')