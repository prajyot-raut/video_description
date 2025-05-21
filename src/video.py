from scenedetect import detect, AdaptiveDetector
from utils import get_images_from_folder
import cv2
import os


def extract_frames(video_path: str, output_dir: str = "video_frames") -> list[str]:
    """
    Extract frames where scene is changing from a video file and save them to a specified directory.

    Args:
        video_path: Path to the input video file.
        output_dir: Directory where the extracted frames will be saved.

    Returns:
        A list of paths to the extracted frame images.
    """
    os.makedirs(output_dir, exist_ok=True)

    # Empty the output directory
    for f in os.listdir(output_dir):
        os.remove(os.path.join(output_dir, f))

    # Returns a list of Scene(start_time, end_time) tuples
    scene_list = detect(video_path, AdaptiveDetector())

    # Open video capture
    video = cv2.VideoCapture(video_path)

    # For each scene boundary, extract the first frame of the new scene
    for idx, scene in enumerate(scene_list, start=1):
        # Compute the frame number at the start of this scene
        frame_id = scene[0].get_frames()  # start frame of the scene
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
        success, frame = video.read()
        if not success:
            continue

        # Save the frame as an image
        filename = os.path.join(output_dir, f"scene_{idx:03d}_frame_{frame_id}.jpg")
        cv2.imwrite(filename, frame)

    video.release()
    print(f"Saved {len(scene_list)} cut-point frames to '{output_dir}/'")
    
    return get_images_from_folder(output_dir)
