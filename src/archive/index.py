from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
LOCAL_IMAGE_PATH = "./data/img.jpg"

def describe_local_image(api_key: str, image_path: str) -> str:
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    # Wrap the raw bytes into a Part object with the correct MIME type
    image_part = types.Part.from_bytes(
        data=image_bytes,
        mime_type="image/jpeg"
    )

    # Initialize the Gemini client
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            "Describe this image in detail:",
            image_part
        ]
    )

    return response.text

if __name__ == "__main__":
    description = describe_local_image(API_KEY, LOCAL_IMAGE_PATH)
    print("Image description:")
    print(description)
