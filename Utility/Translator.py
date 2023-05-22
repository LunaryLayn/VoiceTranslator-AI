import requests
import json

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
        return translation
    else:
        raise Exception("Translation failed with status code: " + str(response.status_code))
    
    
    