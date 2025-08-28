import cv2
import numpy as np
from pathlib import Path
from .utils import validate_image, create_output_path

class ImageToSketchConverter:
    """
    A class to convert images to pencil sketches using OpenCV.
    
    Attributes:
        blur_kernel_size (int): Size of the Gaussian blur kernel
        scale (float): Scale factor for the division operation
    """
    
    def __init__(self, blur_kernel_size=21, scale=256.0):
        """
        Initialize the ImageToSketchConverter.
        
        Args:
            blur_kernel_size (int, optional): Size of the Gaussian blur kernel. 
                                              Must be an odd number. Defaults to 21.
            scale (float, optional): Scale factor for the division operation. 
                                     Defaults to 256.0.
        """
        if blur_kernel_size % 2 == 0:
            raise ValueError("blur_kernel_size must be an odd number")
            
        self.blur_kernel_size = blur_kernel_size
        self.scale = scale
    
    def convert(self, image_path, output_path=None):
        """
        Convert an image to pencil sketch.
        
        Args:
            image_path (str): Path to the input image
            output_path (str, optional): Path to save the output sketch. 
                                         If None, a default path will be created.
        
        Returns:
            numpy.ndarray: The sketch image as a numpy array
        """
        # Validate input image
        validate_image(image_path)
        
        # Create output path if not provided
        if output_path is None:
            output_path = create_output_path(image_path)
        
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Could not read image from {image_path}")
        
        # Convert to grayscale
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Invert the grayscale image
        inverted = cv2.bitwise_not(gray_img)
        
        # Apply Gaussian blur
        blur = cv2.GaussianBlur(inverted, (self.blur_kernel_size, self.blur_kernel_size), 0)
        
        # Invert the blurred image
        inverted_blur = cv2.bitwise_not(blur)
        
        # Create sketch
        sketch = cv2.divide(gray_img, inverted_blur, scale=self.scale)
        
        # Save the result
        cv2.imwrite(output_path, sketch)
        
        return sketch
    
    def convert_batch(self, image_paths, output_dir=None):
        """
        Convert multiple images to pencil sketches.
        
        Args:
            image_paths (list): List of paths to input images
            output_dir (str, optional): Directory to save output sketches.
                                        If None, outputs will be saved alongside inputs.
        
        Returns:
            dict: Mapping of input paths to output paths
        """
        results = {}
        
        for image_path in image_paths:
            if output_dir:
                output_path = Path(output_dir) / f"{Path(image_path).stem}_sketch.png"
            else:
                output_path = None
                
            sketch = self.convert(image_path, output_path)
            results[image_path] = output_path if output_path else create_output_path(image_path)
        
        return results


def convert_image_to_sketch(image_path, output_path=None, blur_kernel_size=21, scale=256.0):
    """
    Convenience function for one-time image to sketch conversion.
    
    Args:
        image_path (str): Path to the input image
        output_path (str, optional): Path to save the output sketch
        blur_kernel_size (int, optional): Size of the Gaussian blur kernel. Defaults to 21.
        scale (float, optional): Scale factor for the division operation. Defaults to 256.0.
    
    Returns:
        numpy.ndarray: The sketch image as a numpy array
    """
    converter = ImageToSketchConverter(blur_kernel_size, scale)
    return converter.convert(image_path, output_path)