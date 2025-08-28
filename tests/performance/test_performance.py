import pytest
import time
import cv2
import numpy as np
import tempfile
import os
from pathlib import Path
from src.converter import ImageToSketchConverter

def create_test_image(size, tmp_path):
    """Create a test image of specified size."""
    img = np.random.randint(0, 255, (size, size, 3), dtype=np.uint8)
    
    test_image_path = tmp_path / f"test_{size}.jpg"
    cv2.imwrite(str(test_image_path), img)
    return str(test_image_path)

@pytest.mark.parametrize("image_size", [256, 512, 1024])
def test_conversion_performance(image_size, tmp_path):
    """Test conversion performance with different image sizes."""
    # Create test image
    test_image = create_test_image(image_size, tmp_path)
    
    # Time the conversion
    converter = ImageToSketchConverter()
    
    start_time = time.time()
    output_path = tmp_path / f"perf_test_{image_size}.png"
    converter.convert(test_image, str(output_path))
    end_time = time.time()
    
    conversion_time = end_time - start_time
    
    # Verify the conversion completed and output was created
    assert output_path.exists()
    
    # Log performance (this could be used for benchmarking)
    print(f"Conversion time for {image_size}x{image_size} image: {conversion_time:.3f}s")

def test_batch_performance(tmp_path):
    """Test batch conversion performance."""
    # Create multiple test images
    image_paths = []
    for i in range(5):
        img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        temp_path = tmp_path / f"perf_batch_{i}.jpg"
        cv2.imwrite(str(temp_path), img)
        image_paths.append(str(temp_path))
    
    # Time the batch conversion
    converter = ImageToSketchConverter()
    
    start_time = time.time()
    results = converter.convert_batch(image_paths, str(tmp_path))
    end_time = time.time()
    
    batch_time = end_time - start_time
    
    # Verify all conversions completed
    assert len(results) == 5
    for output_path in results.values():
        assert Path(output_path).exists()
    
    print(f"Batch conversion time for 5 images: {batch_time:.3f}s")