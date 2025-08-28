import pytest
import cv2
import numpy as np
from pathlib import Path
from src.converter import ImageToSketchConverter, convert_image_to_sketch

@pytest.fixture
def sample_image(tmp_path):
    """Create a sample test image."""
    img = np.ones((100, 100, 3), dtype=np.uint8) * 255
    cv2.circle(img, (50, 50), 30, (0, 0, 255), -1)
    
    image_path = tmp_path / "test_image.jpg"
    cv2.imwrite(str(image_path), img)
    return str(image_path)

def test_converter_initialization():
    """Test that the converter initializes with correct parameters."""
    converter = ImageToSketchConverter(blur_kernel_size=15, scale=300.0)
    assert converter.blur_kernel_size == 15
    assert converter.scale == 300.0

def test_converter_initialization_with_even_kernel():
    """Test that the converter raises error for even kernel size."""
    with pytest.raises(ValueError, match="blur_kernel_size must be an odd number"):
        ImageToSketchConverter(blur_kernel_size=10)

def test_convert_image_to_sketch_function(sample_image, tmp_path):
    """Test the convenience function."""
    output_path = tmp_path / "test_sketch.png"
    sketch = convert_image_to_sketch(sample_image, str(output_path), 21, 256.0)
    
    assert sketch is not None
    assert output_path.exists()
    assert sketch.shape == (100, 100)  # Should be grayscale

def test_convert_method(sample_image, tmp_path):
    """Test the convert method of ImageToSketchConverter."""
    converter = ImageToSketchConverter(blur_kernel_size=21, scale=256.0)
    output_path = tmp_path / "test_sketch.png"
    
    sketch = converter.convert(sample_image, str(output_path))
    
    assert sketch is not None
    assert output_path.exists()
    assert sketch.shape == (100, 100)  # Should be grayscale

def test_convert_method_no_output_path(sample_image):
    """Test the convert method without providing output path."""
    converter = ImageToSketchConverter()
    sketch = converter.convert(sample_image)
    
    # Should create a file with _sketch suffix
    input_path = Path(sample_image)
    expected_path = input_path.parent / f"{input_path.stem}_sketch.png"
    
    assert sketch is not None
    assert expected_path.exists()
    assert sketch.shape == (100, 100)
    
    # Clean up
    if expected_path.exists():
        expected_path.unlink()

def test_convert_batch_method(sample_image, tmp_path):
    """Test the convert_batch method."""
    converter = ImageToSketchConverter()
    
    # Create multiple copies of the sample image
    image_paths = []
    for i in range(3):
        img = cv2.imread(sample_image)
        temp_path = tmp_path / f"test_{i}.jpg"
        cv2.imwrite(str(temp_path), img)
        image_paths.append(str(temp_path))
    
    results = converter.convert_batch(image_paths, str(tmp_path))
    
    assert len(results) == 3
    for input_path, output_path in results.items():
        assert Path(output_path).exists()
        assert "_sketch" in str(output_path)  # Convert to string for the check

def test_sketch_quality(sample_image, tmp_path):
    """Test that the sketch conversion produces a valid result."""
    converter = ImageToSketchConverter()
    output_path = tmp_path / "test_sketch.png"
    sketch = converter.convert(sample_image, str(output_path))
    
    # Sketch should have the same dimensions as input (but grayscale)
    original = cv2.imread(sample_image)
    assert sketch.shape[:2] == original.shape[:2]
    
    # Sketch should be a 2D array (grayscale)
    assert len(sketch.shape) == 2
    
    # Sketch should have values between 0 and 255
    assert sketch.min() >= 0
    assert sketch.max() <= 255