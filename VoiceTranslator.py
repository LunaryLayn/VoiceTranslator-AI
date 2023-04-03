import Recorder
import Transcriber
import Translator
import VoiceSpeaker


URL = input("URL de VoiceVox: ")

Recorder.record()
transcription = Transcriber.transcribe()
JAtranslation = Translator.translate(transcription, "JA")
VoiceSpeaker.speak(JAtranslation, URL)
