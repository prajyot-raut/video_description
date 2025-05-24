import os
from groq import Groq
from audio_extract import extract_audio
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    video_file = "./data/video.mp4"
    audio_file = "./data/audio.wav"

    # 1) Extract audio
    extract_audio(video_file, audio_file, output_format="wav",overwrite=True)

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    filename = "./data/audio.wav"

    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
        file=(filename, file.read()),
        model="whisper-large-v3",
        response_format="verbose_json",
        )
        print(transcription.text)