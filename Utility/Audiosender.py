import sounddevice as sd
import soundfile as sf

def play_audio(file):
    data, fs = sf.read(file, dtype='float32') # lee el archivo de audio
    sd.play(data, fs) # reproduce el audio
    sd.wait() # espera a que termine la reproducción

if __name__ == "__main__":
    audio_file = "audio.mp3" # nombre del archivo de audio generado previamente
    output_device = "Cable Output" # nombre del dispositivo de audio virtual de salida

    play_audio(audio_file) # reproduce el audio generado previamente

    # enruta el audio a través del dispositivo de audio virtual de salida
    with sf.SoundFile(output_device, mode='w', samplerate=44100, channels=2, subtype=None) as f:
        with sd.InputStream(samplerate=44100, channels=2):
            while True:
                data = sd.rec(1024, blocking=True)
                f.write(data)
