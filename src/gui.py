"""
GUI module for the Image to Pencil Sketch converter using Tkinter.
"""
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import cv2
from pathlib import Path
from .converter import ImageToSketchConverter
from .utils import validate_image, create_output_path

class SketchConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Pencil Sketch Converter")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Variables
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.blur_kernel_size = tk.IntVar(value=21)
        self.scale = tk.DoubleVar(value=256.0)
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input section
        ttk.Label(main_frame, text="Input Image:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.input_path, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_input).grid(row=0, column=2, padx=5)
        
        # Output section
        ttk.Label(main_frame, text="Output Image:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.output_path, width=50).grid(row=1, column=1, padx=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_output).grid(row=1, column=2, padx=5)
        
        # Parameters section
        params_frame = ttk.LabelFrame(main_frame, text="Conversion Parameters", padding="10")
        params_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(params_frame, text="Blur Kernel Size:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Spinbox(params_frame, from_=3, to=101, increment=2, textvariable=self.blur_kernel_size, width=10).grid(row=0, column=1, padx=5)
        
        ttk.Label(params_frame, text="Scale Factor:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Spinbox(params_frame, from_=1, to=1000, increment=10, textvariable=self.scale, width=10).grid(row=1, column=1, padx=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=10)
        
        ttk.Button(button_frame, text="Convert", command=self.convert).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Exit", command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
        # Image preview
        preview_frame = ttk.LabelFrame(main_frame, text="Preview", padding="10")
        preview_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        self.original_label = ttk.Label(preview_frame, text="Original Image")
        self.original_label.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.sketch_label = ttk.Label(preview_frame, text="Sketch Image")
        self.sketch_label.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
    def browse_input(self):
        file_path = filedialog.askopenfilename(
            title="Select Input Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
        )
        if file_path:
            self.input_path.set(file_path)
            # Auto-generate output path
            if not self.output_path.get():
                self.output_path.set(create_output_path(file_path))
            self.preview_image(file_path, self.original_label)
    
    def browse_output(self):
        file_path = filedialog.asksaveasfilename(
            title="Save Sketch As",
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
        )
        if file_path:
            self.output_path.set(file_path)
    
    def preview_image(self, image_path, label):
        try:
            image = Image.open(image_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)
            label.configure(image=photo)
            label.image = photo
        except Exception as e:
            messagebox.showerror("Error", f"Could not preview image: {e}")
    
    def convert(self):
        try:
            input_path = self.input_path.get()
            output_path = self.output_path.get()
            
            if not input_path:
                messagebox.showerror("Error", "Please select an input image")
                return
            
            if not output_path:
                messagebox.showerror("Error", "Please select an output path")
                return
            
            validate_image(input_path)
            
            converter = ImageToSketchConverter(
                self.blur_kernel_size.get(),
                self.scale.get()
            )
            
            sketch = converter.convert(input_path, output_path)
            
            # Preview the sketch
            self.preview_image(output_path, self.sketch_label)
            
            messagebox.showinfo("Success", f"Sketch saved to {output_path}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {e}")
    
    def reset(self):
        self.input_path.set("")
        self.output_path.set("")
        self.blur_kernel_size.set(21)
        self.scale.set(256.0)
        self.original_label.configure(image='', text="Original Image")
        self.sketch_label.configure(image='', text="Sketch Image")

def create_gui():
    """Create and run the GUI for the image to sketch converter."""
    root = tk.Tk()
    app = SketchConverterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    create_gui()