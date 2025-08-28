"""
Image to Pencil Sketch Converter

A professional Python package for converting images to pencil sketches
using OpenCV and computer vision techniques.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .converter import ImageToSketchConverter, convert_image_to_sketch
from .utils import validate_image, create_output_path, display_images, get_image_info

__all__ = [
    'ImageToSketchConverter',
    'convert_image_to_sketch',
    'validate_image',
    'create_output_path',
    'display_images',
    'get_image_info'
]