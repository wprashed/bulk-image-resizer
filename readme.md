# Bulk Image Resizer

This Python script resizes images in bulk from an input folder to a specified size and saves them in an output folder. The script supports `.jpg`, `.jpeg`, and `.png` image formats. It's useful for resizing large numbers of images quickly and easily.

## Features
- Resizes multiple images in a batch.
- Supports `.jpg`, `.jpeg`, and `.png` file formats.
- Resize to exact dimensions.
- Saves resized images in a separate output folder.

## Requirements
- Python 3.x
- `Pillow` library (Python Imaging Library)

## Installation

1. **Install Python:** Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Pillow Library:** Install the required Python library using pip.

    ```bash
    pip install pillow
    ```

## Configuration

1. Set the following variables in the script:
    - `INPUT_FOLDER`: Directory containing the images you want to resize.
    - `OUTPUT_FOLDER`: Directory where the resized images will be saved.
    - `NEW_SIZE`: The new dimensions to which the images will be resized (width, height).

2. The script will resize all images in the `INPUT_FOLDER` to the dimensions specified in `NEW_SIZE` and save them in the `OUTPUT_FOLDER`.

## Usage

1. **Prepare your images:** Place all the images you want to resize in the `input_images` folder (or the folder specified in the `INPUT_FOLDER` variable).

2. **Run the script:**

    ```bash
    python app.py
    ```

    The script will process all `.jpg`, `.jpeg`, and `.png` images in the input folder, resize them, and save them in the output folder.

3. **Output Folder:** After running the script, you'll find the resized images in the `output_images` folder (or the folder specified in the `OUTPUT_FOLDER` variable).

## Example Directory Structure

```
input_images/
    image1.jpg
    image2.png
    image3.jpeg
output_images/
    image1.jpg
    image2.png
    image3.jpeg
```

## Notes
- The script automatically creates the output folder (`output_images`) if it does not exist.
- All images are resized to the exact dimensions specified in the `NEW_SIZE` variable.
- It will process all images in the `INPUT_FOLDER` that have `.jpg`, `.jpeg`, or `.png` extensions.

## License
This script is free to use under the MIT License.