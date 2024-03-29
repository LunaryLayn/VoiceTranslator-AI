import whisper

def transcribe(filepath):
    model = whisper.load_model("small")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(filepath)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect a list of languages and their probabilities
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    #options = whisper.DecodingOptions()
    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(result.text)
    return result.text