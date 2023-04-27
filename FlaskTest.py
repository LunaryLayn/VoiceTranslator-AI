from flask import Flask, request, send_file
import Recorder
import Transcriber
import Translator
import VoiceSpeaker
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
    audio_file.save('./test.mp3')

    return 'Archivo de audio guardado correctamente', 200

@app.route('/return_audio', methods=['GET'])
def return_audio():
    transcription = Transcriber.transcribe("test.mp3")
    JAtranslation = Translator.translate(transcription, "JA")
    VoiceSpeaker.speak(JAtranslation, URL)
    return send_file("audio.wav", as_attachment=True)

http_tunnel = ngrok.connect(5000, "http")
print("URL del túnel HTTP:", http_tunnel.public_url)
def shutdown():
    ngrok.disconnect(http_tunnel.public_url)
    ngrok.kill()
atexit.register(shutdown)

#sendEmail(http_tunnel.public_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0')