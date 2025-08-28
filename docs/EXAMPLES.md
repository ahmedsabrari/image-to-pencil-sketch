# Usage Examples - Image to Pencil Sketch Converter

## Basic Usage

### Command Line Interface

1. **Basic conversion:**
   ```bash
   image-to-sketch input.jpg
   ```

2. **Specify output path:**
   ```bash
   image-to-sketch input.jpg -o output_sketch.png
   ```

3. **Custom parameters:**
   ```bash
   image-to-sketch input.jpg -b 31 -s 300.0
   ```

4. **Display result:**
   ```bash
   image-to-sketch input.jpg --display
   ```

5. **Verbose output:**
   ```bash
   image-to-sketch input.jpg -v
   ```

### Python API

#### Basic conversion
```python
from image_to_pencil_sketch import convert_image_to_sketch

# Convert image with default parameters
sketch = convert_image_to_sketch("input.jpg")
```

#### Custom parameters
```python
from image_to_pencil_sketch import convert_image_to_sketch

# Convert with custom parameters
sketch = convert_image_to_sketch(
    "input.jpg", 
    output_path="sketch.png",
    blur_kernel_size=31,
    scale=300.0
)
```

#### Using the class directly
```python
from image_to_pencil_sketch import ImageToSketchConverter

# Create converter instance
converter = ImageToSketchConverter(blur_kernel_size=31, scale=300.0)

# Convert single image
sketch = converter.convert("input.jpg", "output.png")

# Convert multiple images
results = converter.convert_batch(["img1.jpg", "img2.jpg"], "output_directory")
```

## Advanced Examples

### Batch Processing
```python
from image_to_pencil_sketch import ImageToSketchConverter
import glob

# Get all JPEG images in a directory
image_files = glob.glob("images/*.jpg")

# Create converter
converter = ImageToSketchConverter()

# Process all images
results = converter.convert_batch(image_files, "sketches")

print(f"Processed {len(results)} images")
```

### Integration with Web Applications
```python
from image_to_pencil_sketch import convert_image_to_sketch
import cv2
from flask import Flask, request, send_file
import tempfile
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_image():
    if 'image' not in request.files:
        return "No image provided", 400
    
    image_file = request.files['image']
    
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp:
        image_file.save(tmp.name)
        input_path = tmp.name
    
    # Create output path
    output_path = os.path.join(tempfile.gettempdir(), 'sketch.jpg')
    
    # Convert image
    try:
        convert_image_to_sketch(input_path, output_path)
        return send_file(output_path, mimetype='image/jpeg')
    finally:
        # Clean up temporary files
        os.unlink(input_path)
        if os.path.exists(output_path):
            os.unlink(output_path)

if __name__ == '__main__':
    app.run(debug=True)
```

### Integration with GUI Applications
```python
from image_to_pencil_sketch import convert_image_to_sketch
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

class SketchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Sketch Converter")
        
        # Create UI elements
        self.select_btn = tk.Button(root, text="Select Image", command=self.select_image)
        self.select_btn.pack(pady=10)
        
        self.convert_btn = tk.Button(root, text="Convert to Sketch", command=self.convert_image)
        self.convert_btn.pack(pady=10)
        
        self.original_label = tk.Label(root)
        self.original_label.pack(side=tk.LEFT, padx=10)
        
        self.sketch_label = tk.Label(root)
        self.sketch_label.pack(side=tk.RIGHT, padx=10)
        
        self.image_path = None
    
    def select_image(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")]
        )
        if self.image_path:
            self.display_image(self.image_path, self.original_label)
    
    def convert_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first")
            return
        
        try:
            # Convert image
            sketch = convert_image_to_sketch(self.image_path)
            
            # Display sketch
            sketch_rgb = cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB)
            self.display_array(sketch_rgb, self.sketch_label)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert image: {str(e)}")
    
    def display_image(self, path, label):
        img = Image.open(path)
        img.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(img)
        label.configure(image=photo)
        label.image = photo
    
    def display_array(self, array, label):
        img = Image.fromarray(array)
        img.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(img)
        label.configure(image=photo)
        label.image = photo

if __name__ == "__main__":
    root = tk.Tk()
    app = SketchApp(root)
    root.mainloop()
```

## Performance Tips

1. **For large images**, consider resizing before conversion:
   ```python
   import cv2
   from image_to_pencil_sketch import convert_image_to_sketch
   
   # Load and resize image
   image = cv2.imread("large_image.jpg")
   resized = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
   
   # Save resized image temporarily
   cv2.imwrite("temp.jpg", resized)
   
   # Convert resized image
   sketch = convert_image_to_sketch("temp.jpg")
   ```

2. **For batch processing**, reuse the converter instance:
   ```python
   from image_to_pencil_sketch import ImageToSketchConverter
   
   converter = ImageToSketchConverter()
   
   # Reuse the same instance for multiple conversions
   for image_path in image_paths:
       sketch = converter.convert(image_path)
   ```

3. **Adjust parameters** based on image characteristics:
   - Use larger blur kernel size (e.g., 31) for detailed images
   - Use smaller blur kernel size (e.g., 15) for simpler images
   - Adjust scale value to control contrast

## Troubleshooting

### Common Issues

1. **"Could not read image" error**
   - Check that the file exists and path is correct
   - Verify the image format is supported (JPEG, PNG, BMP)

2. **Blur kernel size must be odd**
   - Ensure the blur parameter is an odd number

3. **Output image is too dark/light**
   - Adjust the scale parameter (higher values = lighter output)

4. **Sketch lacks detail**
   - Try a smaller blur kernel size
   - Or try a larger scale value

### Getting Help

If you encounter issues not covered here:
1. Check the API documentation for detailed parameter information
2. Verify your OpenCV installation is working correctly
3. Ensure you're using a supported Python version (3.7+)
