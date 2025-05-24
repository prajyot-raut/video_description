# Video Description Generator

This project automatically generates a textual description of a video file.

## Features

- **Scene Detection**: Identifies significant scene changes in the video to extract relevant frames.
- **Audio Transcription**: Transcribes the audio from the video into text.
- **AI-Powered Description**: Generate detailed descriptions of the video content, incorporating both visual frames and transcribed audio.

## Prerequisites

- Python 3.x
- FFmpeg (must be installed and accessible in your system's PATH for `scenedetect` and `audio-extract` to work correctly)

## Setup

1.  **Clone the repository (if applicable):**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory of the project and add your API keys:
    ```env
    // filepath: .env
    GEMINI_API_KEY=your_gemini_api_key
    GROQ_API_KEY=your_groq_api_key
    ```
    Replace `your_gemini_api_key` and `your_groq_api_key` with your actual API keys.

## Usage

1.  **Place your video file** in the `data/` directory (e.g., `data/my_video.mp4`).
2.  **Update the `VIDEO_PATH`** variable in [`main.py`](e%3A%2FPython%2Fvideo_desc%2Fmain.py) to point to your video file:
    ```python
    // filepath: e:\Python\video_desc\main.py
    // ...existing code...
    VIDEO_PATH = "data/your_video_file.mp4" // Update this line
    // ...existing code...
    ```
3.  **Run the main script:**
    ```bash
    python main.py
    ```
    The script will:
    - Extract frames into `data/video_frames/`.
    - Extract and save audio to `data/audio.wav`.
    - Print the audio transcription to the console.
    - Print the AI-generated description of the video to the console.
