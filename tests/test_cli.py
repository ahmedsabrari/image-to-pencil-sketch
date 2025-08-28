import pytest
import subprocess
import sys
import os
from pathlib import Path
import cv2
import numpy as np

@pytest.fixture
def sample_image(tmp_path):
    """Create a sample test image."""
    img = np.ones((100, 100, 3), dtype=np.uint8) * 255
    cv2.circle(img, (50, 50), 30, (0, 0, 255), -1)
    
    image_path = tmp_path / "test_image.jpg"
    cv2.imwrite(str(image_path), img)
    return str(image_path)

def test_cli_without_args():
    """Test that CLI shows help when run without arguments."""
    result = subprocess.run(
        [sys.executable, "-m", "src.cli"],
        capture_output=True,
        text=True
    )
    
    assert result.returncode != 0
    assert "usage:" in result.stderr.lower()

def test_cli_with_help():
    """Test that CLI shows help with --help flag."""
    result = subprocess.run(
        [sys.executable, "-m", "src.cli", "--help"],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert "convert images to pencil sketches" in result.stdout.lower()

def test_cli_with_valid_image(sample_image, tmp_path):
    """Test that CLI works with a valid image."""
    output_path = tmp_path / "cli_test_output.png"
    
    result = subprocess.run(
        [sys.executable, "-m", "src.cli", sample_image, "-o", str(output_path)],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert output_path.exists()

def test_cli_with_invalid_image():
    """Test that CLI handles invalid image gracefully."""
    result = subprocess.run(
        [sys.executable, "-m", "src.cli", "nonexistent.jpg"],
        capture_output=True,
        text=True
    )
    
    assert result.returncode != 0
    assert "error" in result.stderr.lower()

def test_cli_with_custom_parameters(sample_image, tmp_path):
    """Test that CLI works with custom parameters."""
    output_path = tmp_path / "cli_custom_test.png"
    
    result = subprocess.run(
        [
            sys.executable, "-m", "src.cli", 
            sample_image, 
            "-o", str(output_path),
            "-b", "15",
            "-s", "300.0",
            "-v"
        ],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0
    assert output_path.exists()
    assert "processing" in result.stdout.lower()