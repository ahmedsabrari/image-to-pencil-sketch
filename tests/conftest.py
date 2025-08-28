import pytest
import cv2
import numpy as np
import tempfile
import os
from pathlib import Path

@pytest.fixture
def sample_image():
    """Create a sample test image."""
    # Create a simple image with a white background and a red circle
    img = np.ones((100, 100, 3), dtype=np.uint8) * 255
    cv2.circle(img, (50, 50), 30, (0, 0, 255), -1)
    
    # Save to a temporary file
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        cv2.imwrite(tmp.name, img)
        tmp_path = tmp.name
    
    yield tmp_path
    
    # Clean up
    if os.path.exists(tmp_path):
        os.unlink(tmp_path)

@pytest.fixture
def sample_image_gray():
    """Create a sample grayscale test image."""
    # Create a simple grayscale image with gradient
    img = np.zeros((50, 50), dtype=np.uint8)
    for i in range(50):
        img[i, :] = i * 5
    
    # Save to a temporary file
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
        cv2.imwrite(tmp.name, img)
        tmp_path = tmp.name
    
    yield tmp_path
    
    # Clean up
    if os.path.exists(tmp_path):
        os.unlink(tmp_path)

@pytest.fixture
def output_dir():
    """Create a temporary output directory."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield tmp_dir