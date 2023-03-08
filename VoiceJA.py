from voicevox import Client
import asyncio
from pydub import AudioSegment
from pydub.playback import play

async def main():
    async with Client() as client:
        audio_query = await client.create_audio_query(
            "こんにちは！", speaker=1
        )
        with open("voice.wav", "wb") as f:
            f.write(await audio_query.synthesis())

        # Load the generated audio file and play it
        audio_file = AudioSegment.from_wav("voice.wav")
        play(audio_file)

if __name__ == "__main__":
    asyncio.run(main())
