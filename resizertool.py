import os
from PIL import Image

# Configuration
input_folder = 'images/input'         # Folder containing original images
output_folder = 'images/output'       # Folder to save resized images
target_size = (800, 600)              # Desired size (width, height)
output_format = 'JPEG'                # Output format: 'JPEG', 'PNG', etc.

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported image extensions
valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')

# Resize and convert images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_extensions):
        input_path = os.path.join(input_folder, filename)
        output_name = os.path.splitext(filename)[0] + '.' + output_format.lower()
        output_path = os.path.join(output_folder, output_name)

        try:
            with Image.open(input_path) as img:
                resized_img = img.resize(target_size)
                resized_img.save(output_path, output_format)
                print(f"✅ Saved: {output_path}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")
