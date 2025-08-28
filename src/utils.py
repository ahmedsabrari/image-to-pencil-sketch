import os
import cv2
from pathlib import Path

def validate_image(image_path):
    """
    Validate that an image file exists and is readable.
    
    Args:
        image_path (str): Path to the image file
    
    Raises:
        FileNotFoundError: If the image file doesn't exist
        ValueError: If the file is not a supported image format or cannot be read
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    # Check if the file is a supported image format
    supported_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif']
    if Path(image_path).suffix.lower() not in supported_formats:
        raise ValueError(f"Unsupported image format: {Path(image_path).suffix}. "
                         f"Supported formats: {', '.join(supported_formats)}")
    
    # Try to read the image to verify it's valid
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image from {image_path}. File may be corrupted.")

def create_output_path(input_path, suffix="_sketch"):
    """
    Create a default output path based on the input path.
    
    Args:
        input_path (str): Path to the input image
        suffix (str, optional): Suffix to add to the filename. Defaults to "_sketch".
    
    Returns:
        str: Output path for the sketch
    """
    path = Path(input_path)
    # Use PNG format by default for better quality
    output_path = path.parent / f"{path.stem}{suffix}.png"
    return str(output_path)

def display_images(original_path, sketch_path, window_name='Image Comparison'):
    """
    Display the original and sketch images side by side.
    
    Args:
        original_path (str): Path to the original image
        sketch_path (str): Path to the sketch image
        window_name (str, optional): Name of the display window. Defaults to 'Image Comparison'.
    """
    # Read images
    original = cv2.imread(original_path)
    sketch = cv2.imread(sketch_path)
    
    if original is None:
        raise ValueError(f"Could not read original image from {original_path}")
    if sketch is None:
        raise ValueError(f"Could not read sketch image from {sketch_path}")
    
    # Resize images to have the same height for comparison
    height = min(original.shape[0], sketch.shape[0])
    width1 = int(original.shape[1] * height / original.shape[0])
    width2 = int(sketch.shape[1] * height / sketch.shape[0])
    
    original_resized = cv2.resize(original, (width1, height))
    sketch_resized = cv2.resize(sketch, (width2, height))
    
    # Concatenate images horizontally
    comparison = cv2.hconcat([original_resized, sketch_resized])
    
    # Add labels
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(comparison, 'Original', (10, 30), font, 1, (0, 0, 255), 2)
    cv2.putText(comparison, 'Sketch', (width1 + 10, 30), font, 1, (0, 0, 255), 2)
    
    # Display the comparison
    cv2.imshow(window_name, comparison)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_image_info(image_path):
    """
    Get information about an image.
    
    Args:
        image_path (str): Path to the image file
    
    Returns:
        dict: Information about the image (dimensions, channels, etc.)
    """
    image = cv2.imread(image_path)
    if image is None:
        return None
    
    return {
        'path': image_path,
        'dimensions': image.shape[:2],
        'channels': image.shape[2] if len(image.shape) > 2 else 1,
        'size_bytes': os.path.getsize(image_path),
        'format': Path(image_path).suffix.lower()
    }