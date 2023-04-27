import Recorder
import Transcriber
import Translator
import VoiceSpeaker
#docker voicevox: docker run --rm --gpus all -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
#ngrok http 50021
print("Bienvenido a VoiceTranslator: Recuerda abrir VoiceVox en Google Collab para obtener la URL: https://colab.research.google.com/drive/1nwWSLQN7_dPS5Dq4EAXg3hLrkfrDFbLi#scrollTo=TlYOWAolCjq-")
URL = input("URL de VoiceVox: ")

while True:
    Recorder.record()
    transcription = Transcriber.transcribe()
    JAtranslation = Translator.translate(transcription, "JA")
    VoiceSpeaker.speak(JAtranslation, URL)
