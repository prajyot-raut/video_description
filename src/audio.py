import os
from groq import Groq
from audio_extract import extract_audio
from dotenv import load_dotenv

load_dotenv()

def transcribe_audio(video_path: str, audio_path: str = "./data/audio.wav") -> str:
    """
    Transcribe audio from a file using Groq's Whisper model.
    
    Args:
        filename (str): Path to the audio file.
        
    Returns:
        str: Transcription of the audio.
    """

    # Extract audio
    extract_audio(video_path, audio_path, output_format="wav",overwrite=True)

    # transcribe audio using Groq
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError("GROQ_API_KEY environment variable is not set.")
    
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    with open(audio_path, "rb") as file:
        transcription = client.audio.transcriptions.create(
        file=(audio_path, file.read()),
        model="whisper-large-v3",
        response_format="verbose_json",
        )
        return (transcription.text)