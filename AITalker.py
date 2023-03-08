#Para utilizarlo hay que descargar e iniciar el Docker de Whisper: https://hub.docker.com/r/onerahmet/openai-whisper-asr-webservice

import pyaudio
import wave
import keyboard
import requests
import json
from voicevox import Client
import asyncio
from pydub import AudioSegment
from pydub.playback import play


# Define audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Initialize Pyaudio
audio = pyaudio.PyAudio()

# Define audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)

frames = []

def recording():
    # Wait for F key press to start recording
    print("Press F to start recording...")
    keyboard.wait('F')

    print("Recording started...")

    # Record audio frames while F key is pressed
    while keyboard.is_pressed('F'):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording stopped...")

    # Stop audio stream and terminate Pyaudio
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save recorded audio to a WAV file
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    print("Audio saved to %s" % WAVE_OUTPUT_FILENAME)
    


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

    translate(response_text, "JA")


def translate(text, target_lang):
    url = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Authorization": "DeepL-Auth-Key 8565974c-4c4f-d541-78ef-6b43dff09274:fx"
    }
    data = {
        "text": text,
        "target_lang": target_lang
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        translation = response.json()["translations"][0]["text"]
        print(translation)
        asyncio.run(synthetize(translation)) 
    else:
        raise Exception("Translation failed with status code: " + str(response.status_code))
    

async def synthetize(Japanese_text):
    async with Client() as client:
        audio_query = await client.create_audio_query(
            Japanese_text, speaker=1
        )
        with open("voice.wav", "wb") as f:
            f.write(await audio_query.synthesis())

        # Load the generated audio file and play it
        audio_file = AudioSegment.from_wav("voice.wav")
        play(audio_file)

recording()
transcribe()