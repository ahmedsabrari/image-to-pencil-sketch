import argparse
import sys
from pathlib import Path
from .converter import ImageToSketchConverter, convert_image_to_sketch
from .utils import validate_image, display_images, create_output_path

def main():
    """Command-line interface for the Image to Pencil Sketch converter."""
    parser = argparse.ArgumentParser(
        description="Convert images to pencil sketches using OpenCV",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m image_to_pencil_sketch.cli input.jpg
  python -m image_to_pencil_sketch.cli input.jpg -o sketch.png
  python -m image_to_pencil_sketch.cli input.jpg -b 31 -s 300.0 --display
        """
    )
    
    parser.add_argument("input", help="Path to the input image")
    parser.add_argument("-o", "--output", help="Path to save the output sketch")
    parser.add_argument("-b", "--blur", type=int, default=21, 
                        help="Kernel size for Gaussian blur (must be odd, default: 21)")
    parser.add_argument("-s", "--scale", type=float, default=256.0,
                        help="Scale factor for the division operation (default: 256.0)")
    parser.add_argument("-d", "--display", action="store_true",
                        help="Display the original and sketch images side by side")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose output")
    
    args = parser.parse_args()
    
    try:
        # Validate input image
        validate_image(args.input)
        
        if args.verbose:
            print(f"Processing image: {args.input}")
        
        # Determine output path
        output_path = args.output if args.output else create_output_path(args.input)
        
        # Convert image to sketch
        sketch = convert_image_to_sketch(
            args.input, 
            output_path, 
            args.blur, 
            args.scale
        )
        
        if args.verbose:
            print(f"Sketch saved to: {output_path}")
        
        # Display images if requested
        if args.display:
            display_images(args.input, output_path)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()