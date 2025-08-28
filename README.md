# Image to Pencil Sketch Converter

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv" alt="OpenCV Version" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License" />
  <img src="https://img.shields.io/badge/Version-1.0.0-brightgreen?style=for-the-badge" alt="Version" />
  <img src="https://img.shields.io/github/issues/your-username/image-to-pencil-sketch?style=for-the-badge" alt="Issues" />
  <img src="https://img.shields.io/github/stars/your-username/image-to-pencil-sketch?style=for-the-badge" alt="Stars" />
</p>

## 📖 About The Project

A sophisticated Python application that transforms ordinary photographs into beautiful pencil sketch artworks using OpenCV's computer vision capabilities. This tool provides a simple yet powerful way to create artistic representations of your images with realistic sketch effects.

![Example Transformation](https://via.placeholder.com/800x400.png?text=Original+Image+%2B+Sketch+Result)

### Key Features
- 🎨 High-quality pencil sketch conversion
- ⚡ Real-time processing capabilities
- 🖼️ Support for multiple image formats (JPEG, PNG, BMP, TIFF)
- 💾 Automatic saving of results
- 🎚️ Customizable sketch parameters
- 🖥️ Command-line interface for easy integration
- 🐍 Clean, object-oriented Python API

## 🚀 Built With

- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) Python 3.7+
- ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white) OpenCV 4.x
- ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) NumPy

## 📋 Prerequisites

Before installation, ensure you have met the following requirements:

- Python 3.7 or higher
- pip package manager
- GCC/g++ compiler (for OpenCV installation on Linux)

## ⚙️ Installation

### Method 1: Install from PyPI (Recommended)

```bash
pip install image-to-pencil-sketch
```

### Method 2: Install from Source

1. **Clone the repository**
```bash
git clone https://github.com/ahmedsabrari/image-to-pencil-sketch.git
cd image-to-pencil-sketch
```

2. **Install the package**
```bash
pip install -e .
```

## 🎯 Usage

### Command Line Interface

```bash

```

### Python API

```python
from image_to_pencil_sketch import ImageToSketchConverter, convert_image_to_sketch

# Using the convenience function
sketch = convert_image_to_sketch("input.jpg", "output.png")

# Using the class-based approach
converter = ImageToSketchConverter(blur_kernel_size=31, scale=300.0)
sketch = converter.convert("input.jpg", "output.png")

# Batch processing
results = converter.convert_batch(["img1.jpg", "img2.jpg"], "output_directory")
```

### Advanced Configuration

```python
# Customize sketch parameters
converter = ImageToSketchConverter(
    blur_kernel_size=21,  # Controls smoothness (must be odd)
    scale=256.0           # Controls contrast
)

# Process multiple images with different settings
for image_path in image_paths:
    # Adjust parameters based on image characteristics
    if is_detailed_image(image_path):
        converter.blur_kernel_size = 31
    else:
        converter.blur_kernel_size = 21
        
    converter.convert(image_path)
```

## 📁 Project Structure

```
image-to-pencil-sketch/
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── converter.py
│   ├── gui.py
│   └── utils.py
├── tests/
│   ├── integration/
│   │   └── test_integration.py
│   ├── performance/
│   │   └── test_performance.py
│   ├── conftest.py
│   ├── test_cli.py
│   ├── test_converter.py
│   └── test_utils.py
├── samples/
│   ├── input/
│   └── output/
├── images/
│   └── demo.png
├── docs/
│   ├── API.md
│   ├── INSTALLATION.md
│   └── EXAMPLES.md
├── .gitignore
├── .pre-commit-config.yaml
├── requirements.txt
├── setup.py
├── pyproject.toml
├── LICENSE
└── README.md
```

## 🧪 Testing

To run the test suite:

```bash

```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🗺️ Roadmap

- [ ] GUI interface using Tkinter/PyQt
- [ ] Web application using Flask/Django
- [ ] Mobile app implementation
- [ ] AI-enhanced sketch quality improvement
- [ ] Batch processing GUI
- [ ] Plugin support for image editors

See the [open issues](https://github.com/your-username/image-to-pencil-sketch/issues) for a full list of proposed features (and known issues).

## ❓ FAQ

### Q: What image formats are supported?
A: All formats supported by OpenCV: JPEG, PNG, BMP, TIFF, and more.

### Q: Can I adjust the sketch intensity?
A: Yes, by modifying the blur_kernel_size and scale parameters.

### Q: Does this work with color images?
A: The conversion process automatically handles color images by converting them to grayscale first.

### Q: How can I improve the sketch quality?
A: Higher resolution input images generally produce better results. You can also experiment with the blur parameters.

### Q: Is this suitable for batch processing?
A: Yes, the library includes a `convert_batch()` method for processing multiple images.

## 📞 Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Project Link: [https://github.com/your-username/image-to-pencil-sketch](https://github.com/your-username/image-to-pencil-sketch)

## 🙏 Acknowledgments

- [OpenCV](https://opencv.org/) for excellent computer vision library
- [NumPy](https://numpy.org/) for numerical computations
- Inspired by various computer vision tutorials and research papers

## 📚 Additional Resources

- [API Documentation](docs/API.md)
- [Usage Examples](docs/EXAMPLES.md)
- [Installation Guide](docs/INSTALLATION.md)

---