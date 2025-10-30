#  Image Resizer Tool

Automate the process of resizing and converting images in bulk using Python and Pillow.

##  Features
- Resize all images in a folder to a target dimension
- Convert images to a specified format (e.g., JPEG, PNG)
- Save resized images to a separate output folder
- Handles multiple image types: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`
- Error handling for corrupted or unsupported files

##  Requirements
- Python 3.11+
- Pillow (Python Imaging Library fork)

Install dependencies:
```bash
pip install pillow
```

##  Folder Structure
```
Image Resizer/
├── resizer.py
├── images/
│   ├── input/      # Place original images here
│   └── output/     # Resized images will be saved here
```

##  How to Run
```bash
python resizer.py
```

Make sure your working directory contains:
- `resizer.py` script
- `images/input/` folder with images to process

##  Configuration
Inside `resizer.py`, you can customize:
```python
target_size = (800, 600)          # Resize dimensions
output_format = 'JPEG'            # Output format: 'JPEG', 'PNG', etc.
input_folder = 'images/input'     # Source folder
output_folder = 'images/output'   # Destination folder
```

##  Concepts Used
- File handling with `os`
- Image processing with `PIL.Image`
- Exception handling with `try-except`

##  Future Enhancements
- Add CLI support with `argparse`
- GUI interface using `tkinter` or `PyQt`
- Drag-and-drop image support
- Resize by percentage or aspect ratio


