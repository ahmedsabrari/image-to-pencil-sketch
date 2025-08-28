import pytest
import tempfile
import os
from pathlib import Path
from src.utils import validate_image, create_output_path, display_images, get_image_info

# ... other tests ...

def test_create_output_path():
    """Test that create_output_path generates correct path."""
    input_path = "/path/to/image.jpg"
    output_path = create_output_path(input_path)
    
    # Use Path objects for comparison to handle OS differences
    assert Path(output_path) == Path("/path/to/image_sketch.png")
    
    # Test with custom suffix
    output_path_custom = create_output_path(input_path, "_pencil")
    assert Path(output_path_custom) == Path("/path/to/image_pencil.png")