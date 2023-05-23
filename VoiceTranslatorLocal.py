from Utility import Recorder
from Utility import Transcriber
from Utility import Translator
from Utility import VoiceSpeaker
from Utility import AudioCabler

#docker voicevox: docker run --rm --gpus all -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
#ngrok http 50021
print("Bienvenido a AITranslator: Recuerda poner la URL de ngrok de Docker generada en el servidor si quieres usarlo remotamente")

#Nota: Si se quiere usar la version remotamente, se debe cambiar la URL a la URL generada por ngrok de VoiceVox en el servidor

URL = "http://127.0.0.1:50021"
while True:
    Recorder.record()
    transcription = Transcriber.transcribe(".\\AudioSources\\output.wav")
    JAtranslation = Translator.translate(transcription, "JA")
    VoiceSpeaker.speak(JAtranslation, URL, False)
    AudioCabler.reproduceInStream()
