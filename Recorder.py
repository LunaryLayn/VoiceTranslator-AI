import pyaudio
import wave
import keyboard

# Define audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

def record():
    # Initialize Pyaudio
    audio = pyaudio.PyAudio()

    # Define audio stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    frames = []

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
