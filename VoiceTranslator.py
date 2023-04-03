import Recorder
import Transcriber
import Translator
import VoiceSpeaker

print("Bienvenido a VoiceTranslator: Recuerda abrir VoiceVox en Google Collab para obtener la URL: https://colab.research.google.com/drive/1nwWSLQN7_dPS5Dq4EAXg3hLrkfrDFbLi#scrollTo=TlYOWAolCjq-")
URL = input("URL de VoiceVox: ")

Recorder.record()
transcription = Transcriber.transcribe()
JAtranslation = Translator.translate(transcription, "JA")
VoiceSpeaker.speak(JAtranslation, URL)
