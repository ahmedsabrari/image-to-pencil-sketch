# Installation Guide - Image to Pencil Sketch Converter

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- GCC/g++ compiler (for Linux systems)

## Installation Methods

### 1. Installation from PyPI (Recommended)

```bash
pip install image-to-pencil-sketch
```

### 2. Installation from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-to-pencil-sketch.git
   cd image-to-pencil-sketch
   ```

2. Install in development mode:
   ```bash
   pip install -e .
   ```

### 3. Using requirements.txt

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Verifying Installation

To verify the installation is working correctly:

```bash
python -c "import image_to_pencil_sketch; print('Installation successful')"
```

Or test the command-line interface:

```bash
image-to-sketch --help
```

## Platform-Specific Notes

### Windows

No special requirements. The package should install without issues.

### macOS

You may need to install OpenCV dependencies:

```bash
brew install opencv
```

### Linux

You may need to install system dependencies:

```bash
# Ubuntu/Debian
sudo apt-get install libopencv-dev python3-opencv

# Fedora
sudo dnf install opencv-devel

# CentOS/RHEL
sudo yum install opencv-devel
```

## Docker Installation

A Dockerfile is provided for containerized deployment:

```bash
# Build the image
docker build -t image-to-sketch .

# Run the container
docker run -v $(pwd):/data image-to-sketch input.jpg
```

## Troubleshooting Installation

### Common Issues

1. **OpenCV installation fails**
   - Try installing the headless version: `pip install opencv-python-headless`

2. **Permission errors**
   - Use a virtual environment to avoid system-wide installation
   - Or use `pip install --user image-to-pencil-sketch`

3. **Missing dependencies**
   - Ensure you have Python development tools installed
   - On Ubuntu: `sudo apt-get install python3-dev`

4. **Import errors**
   - Verify your Python version meets the requirements
   - Check that the package installed correctly with `pip list`

### Getting Help

If you encounter installation issues:

1. Check the [GitHub issues](https://github.com/your-username/image-to-pencil-sketch/issues) for known problems
2. Verify your system meets all prerequisites
3. Ensure you're using a supported Python version

## Uninstallation

To remove the package:

```bash
pip uninstall image-to-pencil-sketch
```

## Development Installation

For contributing to the project:

1. Fork and clone the repository
2. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```
3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```