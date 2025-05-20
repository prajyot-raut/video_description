from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

IMAGE_PATHS = [
    "path/to/image1.jpg",
    "path/to/image2.png",
    "path/to/image3.jpeg",
]

def describe_multiple_images(api_key: str, image_paths: list[str]) -> str:
    image_parts = []

    # Wrap the raw bytes into a Part object with the correct MIME type
    for path in image_paths:
        mime = "image/jpeg" if path.lower().endswith((".jpg", ".jpeg")) else "image/png"
        with open(path, "rb") as f:
            image_bytes = f.read()
        image_parts.append(types.Part.from_bytes(data=image_bytes, mime_type=mime))

    
    client = genai.Client(api_key=api_key)

    prompt = "Please describe each of these images in detail, and label them Image 1, Image 2, etc.:"
    contents = [prompt] + image_parts

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=contents
    )

    return response.text

if __name__ == "__main__":
    desc = describe_multiple_images(API_KEY, IMAGE_PATHS)
    print(desc)
