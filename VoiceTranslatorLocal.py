from Utility import Recorder
from Utility import Transcriber
from Utility import Translator
from Utility import VoiceSpeaker
from Utility import AudioCabler
#docker voicevox: docker run --rm --gpus all -p '127.0.0.1:50021:50021' voicevox/voicevox_engine:nvidia-ubuntu20.04-latest
#ngrok http 50021
#print("Bienvenido a VoiceTranslator: Recuerda abrir VoiceVox en Google Collab para obtener la URL: https://colab.research.google.com/drive/1nwWSLQN7_dPS5Dq4EAXg3hLrkfrDFbLi#scrollTo=TlYOWAolCjq-")

URL = "http://127.0.0.1:50021"
while True:
    Recorder.record()
    transcription = Transcriber.transcribe(".\\AudioSources\\output.wav")
    JAtranslation = Translator.translate(transcription, "JA")
    VoiceSpeaker.speak(JAtranslation, URL, False)
    AudioCabler.reproduceInStream()
