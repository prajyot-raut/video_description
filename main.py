from google import genai
from google.genai import types
from dotenv import load_dotenv
from src.video import extract_frames
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

IMAGE_PATHS = extract_frames("data/sample.mp4")

def describe_multiple_images(api_key: str, image_paths: list[str]) -> str:
    image_parts = []

    # Wrap the raw bytes into a Part object with the correct MIME type
    for path in image_paths:
        mime = "image/jpeg" if path.lower().endswith((".jpg", ".jpeg")) else "image/png"
        with open(path, "rb") as f:
            image_bytes = f.read()
        image_parts.append(types.Part.from_bytes(data=image_bytes, mime_type=mime))

    
    client = genai.Client(api_key=api_key)

    prompt = "I am providing the frame of a video. Describe what is happening in the scene. Be as detailed as possible. The scene is a cut from a video, so please describe the action, characters, and any other relevant details. Also desribe the emotions that video wants to convey (use emojis also)."
    contents = [prompt] + image_parts

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=contents
    )

    return response.text

if __name__ == "__main__":
    desc = describe_multiple_images(API_KEY, IMAGE_PATHS)
    print(desc)
