import speech_recognition as sr
from pydub import AudioSegment
import os

recognizer = sr.Recognizer()
audio_file_path = "./data/audio.wav"

def transcribe_audio_chunks(path_to_audio_file):
    full_transcription = ""
    sound = AudioSegment.from_wav(path_to_audio_file)
    
    # Simple fixed-duration chunks (e.g., 30 seconds)
    chunk_length_ms = 30 * 1000
    chunks = [sound[i:i + chunk_length_ms] for i in range(0, len(sound), chunk_length_ms)]

    if not os.path.exists("data/temp_chunks"):
        os.makedirs("data/temp_chunks")

    for i, audio_chunk in enumerate(chunks):
        chunk_filename = os.path.join("data/temp_chunks", f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_listened)
                print(f"Chunk {i}: {text}")
                full_transcription += text + " "
            except sr.UnknownValueError:
                print(f"Chunk {i}: Could not understand audio")
            except sr.RequestError as e:
                print(f"Chunk {i}: Could not request results; {e}")
        os.remove(chunk_filename) # Clean up chunk file
    
    if os.path.exists("temp_chunks"): # Clean up directory
        os.rmdir("temp_chunks")
        
    return full_transcription.strip()

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    actual_audio_path = os.path.join(project_root, "data", "audio.wav")

    if not os.path.exists(actual_audio_path):
        print(f"Error: Audio file not found at {actual_audio_path}")
    else:
        print("Starting transcription by chunks...")
        transcription = transcribe_audio_chunks(actual_audio_path)
        print("\nFull Transcription:")
        print(transcription)


""" import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.AudioFile("./data/audio.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print("Transcription:", text)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results; {e}") """