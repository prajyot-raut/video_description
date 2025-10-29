from google import genai
from google.genai import types
from dotenv import load_dotenv
from src.video import extract_frames
from src.audio import transcribe_audio
from src.prompt import PROMPT
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

VIDEO_PATH = "data/sample.mp4"

IMAGE_PATHS = extract_frames(VIDEO_PATH)
transcription = transcribe_audio(VIDEO_PATH)

print("Transcription of the video:")
print(transcription)


def describe_multiple_images(api_key: str, image_paths: list[str]) -> str:
    image_parts = []

    # Wrap the raw bytes into a Part object with the correct MIME type
    for path in image_paths:
        mime = "image/jpeg" if path.lower().endswith((".jpg", ".jpeg")) else "image/png"
        with open(path, "rb") as f:
            image_bytes = f.read()
        image_parts.append(types.Part.from_bytes(data=image_bytes, mime_type=mime))

    client = genai.Client(api_key=api_key)

    prompt = PROMPT + transcription + "\n\n"
    contents = [prompt] + image_parts

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=contents
    )

    return response.text


if __name__ == "__main__":
    desc = describe_multiple_images(API_KEY, IMAGE_PATHS)
    print(desc)

    os.makedirs("output", exist_ok=True)
    out_path = os.path.join("output", "output.md")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# Video Description\n\n")
        f.write("## Transcription\n\n")
        f.write(transcription.strip() + "\n\n")
        f.write("## Description\n\n")
        f.write(desc.strip() + "\n")

    print(f"Wrote output to {out_path}")
