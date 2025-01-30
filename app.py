import os
from PIL import Image

# Input and output directories
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
NEW_SIZE = (4000, 2250)  # Set your desired width and height

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(INPUT_FOLDER, filename)
        img = Image.open(img_path)

        # Resize to exact dimensions (Pillow 10+ handles antialiasing by default)
        img_resized = img.resize(NEW_SIZE)

        # Save to output folder
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        img_resized.save(output_path)

        print(f"✅ Resized and saved: {output_path}")

print("✅ Bulk resizing complete!")