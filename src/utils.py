import os

def get_images_from_folder(folder_path: str) -> list[str]:
    """
    Gets a list of image file paths from a specified folder.

    Args:
        folder_path: The path to the folder.

    Returns:
        A list of relative paths to image files within the folder.
        Returns an empty list if the folder doesn't exist or contains no images.
    """
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')
    image_files = []
    if not os.path.isdir(folder_path):
        print(f"Error: Folder not found at {folder_path}")
        return []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(image_extensions):
            image_files.append(os.path.join(folder_path, filename))
    return image_files

