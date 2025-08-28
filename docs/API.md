# API Reference - Image to Pencil Sketch Converter

## Overview

This document provides detailed information about the API for the Image to Pencil Sketch Converter package.

## Core Classes

### ImageToSketchConverter

The main class for converting images to pencil sketches.

#### Constructor
```python
ImageToSketchConverter(blur_kernel_size=21, scale=256.0)
```

**Parameters:**
- `blur_kernel_size` (int): Size of the Gaussian blur kernel (must be odd)
- `scale` (float): Scale factor for the division operation

#### Methods

##### convert()
```python
convert(image_path, output_path=None)
```

Converts a single image to pencil sketch.

**Parameters:**
- `image_path` (str): Path to the input image
- `output_path` (str, optional): Path to save the output sketch

**Returns:**
- `numpy.ndarray`: The sketch image as a numpy array

##### convert_batch()
```python
convert_batch(image_paths, output_dir=None)
```

Converts multiple images to pencil sketches.

**Parameters:**
- `image_paths` (list): List of paths to input images
- `output_dir` (str, optional): Directory to save output sketches

**Returns:**
- `dict`: Mapping of input paths to output paths

## Utility Functions

### validate_image()
```python
validate_image(image_path)
```

Validates that an image file exists and is readable.

**Parameters:**
- `image_path` (str): Path to the image file

**Raises:**
- `FileNotFoundError`: If the image file doesn't exist
- `ValueError`: If the file is not a supported image format

### create_output_path()
```python
create_output_path(input_path, suffix="_sketch")
```

Creates a default output path based on the input path.

**Parameters:**
- `input_path` (str): Path to the input image
- `suffix` (str, optional): Suffix to add to the filename

**Returns:**
- `str`: Output path for the sketch

### display_images()
```python
display_images(original_path, sketch_path, window_name='Image Comparison')
```

Displays the original and sketch images side by side.

**Parameters:**
- `original_path` (str): Path to the original image
- `sketch_path` (str): Path to the sketch image
- `window_name` (str, optional): Name of the display window

## Command Line Interface

The package includes a command-line interface with the following options:

```
usage: image-to-sketch [-h] [-o OUTPUT] [-b BLUR] [-s SCALE] [-d] [-v] input

Convert images to pencil sketches using OpenCV

positional arguments:
  input                 Path to the input image

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Path to save the output sketch
  -b BLUR, --blur BLUR  Kernel size for Gaussian blur (must be odd, default: 21)
  -s SCALE, --scale SCALE
                        Scale factor for the division operation (default: 256.0)
  -d, --display         Display the original and sketch images side by side
  -v, --verbose         Verbose output
```

## Error Handling

The API raises the following exceptions:

- `FileNotFoundError`: When the input image file doesn't exist
- `ValueError`: When the file format is not supported or parameters are invalid
- `Exception`: For any other errors during processing

## Version History

- v1.0.0: Initial release with core functionality
