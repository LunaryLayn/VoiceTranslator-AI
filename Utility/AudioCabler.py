import pyaudio
import wave

def reproduceInStream():# Specify the file path of the audio file
    audio_file = ".\\AudioSources\\audio.wav"

    # Load the audio file
    wf = wave.open(audio_file, 'rb')

    # Create an instance of PyAudio
    audio = pyaudio.PyAudio()

    # Get the desired output device ID or index
    output_device_index = 6
    # Update with the correct index or ID

    # Open the audio stream with the desired output device
    stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output_device_index=output_device_index,
                        output=True)

    # Read the audio data and play it through the virtual cable
    chunk_size = 1024
    data = wf.readframes(chunk_size)
    while data:
        stream.write(data)
        data = wf.readframes(chunk_size)

    # Close the stream and terminate PyAudio
    stream.stop_stream()
    stream.close()
    audio.terminate()

