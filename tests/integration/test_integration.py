import pytest
import cv2
import numpy as np
from pathlib import Path  # Add this import
from src.converter import ImageToSketchConverter
from src.utils import validate_image, display_images, get_image_info