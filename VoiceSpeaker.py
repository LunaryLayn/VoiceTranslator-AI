import requests
import json
from urllib.parse import urlencode
from pydub import AudioSegment
from pydub.playback import play

VOICE_ID=1

# Type: float
SPEED_SCALE=1.0
VOLUME_SCALE=4.0
INTONATION_SCALE=1.5
PRE_PHONEME_LENGTH=1.0
POST_PHONEME_LENGTH=1.0

# API endpoint URL

def speak(text, URL):
    BASE_URL = URL
    # Make a POST request to generate a query
    params_encoded = urlencode({'text': text, 'speaker': VOICE_ID})
    r = requests.post(f'{BASE_URL}/audio_query?{params_encoded}')

    if r.status_code == 404:
        print('Unable to reach Voicevox, ensure that it is running, or the VOICEVOX_BASE_URL variable is set correctly')


    voicevox_query = r.json()
    voicevox_query['speedScale'] = SPEED_SCALE
    voicevox_query['volumeScale'] = VOLUME_SCALE
    voicevox_query['intonationScale'] = INTONATION_SCALE
    voicevox_query['prePhonemeLength'] = PRE_PHONEME_LENGTH
    voicevox_query['postPhonemeLength'] = POST_PHONEME_LENGTH

    # synthesize voice as wav file
    params_encoded = urlencode({'speaker': VOICE_ID})
    r = requests.post(f'{BASE_URL}/synthesis?{params_encoded}', json=voicevox_query)
    # Save the audio to a file
    with open("audio.wav", "wb") as f:
        f.write(r.content)
    audio_file = AudioSegment.from_wav("audio.wav")
    play(audio_file)
    