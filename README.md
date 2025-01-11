# ImgTextify

**ImgTextify** is a Python-based project that utilizes Hugging Face’s BLIP (Bootstrapping Language-Image Pretraining) model to generate captions from images and answer questions about their content. This project demonstrates the power of multimodal learning, bridging the gap between text and image understanding.

## Features

- **Image Captioning**: Generate descriptive captions for images using the BLIP model.
- **Visual Question Answering (VQA)**: Ask questions about images and get accurate responses based on the visual content.

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/ImgTextify.git
cd ImgTextify
```

## Installation

### 2. Set up the Python virtual environment:

Make sure you have **Python 3.7+** installed.

Create a virtual environment:

```bash
python -m venv EnviroPy
```

Activate the virtual environment:
.\EnviroPy\Scripts\Activate

## Usage

### 1. **Image Captioning**

To generate a caption for an image, modify the `image_path` in `src/main.py` to point to the image you want to process. Then run the script:

```bash
python src/main.py

```

### 4. Visualization and Expected Output

Once you run the script, the program will generate a caption for the image and answer any questions you may ask about the image content.

#### Example:

```bash
Generated Caption: A person standing on a mountain peak with a backpack.
Answer: A person standing on a mountain.
```
