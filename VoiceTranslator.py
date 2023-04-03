import Recorder
import Translator
import Transcriber
import SpeakerJA
import asyncio

Recorder.record()
textOrigin = Transcriber.transcribe()
textJA = Translator.translate(textOrigin, "JA")
asyncio.run(SpeakerJA.speak(textJA))