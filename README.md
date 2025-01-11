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

```bash
.\EnviroPy\Scripts\Activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### 1. **Image Captioning**

To generate a caption for an image, modify the `image_path` in `src/main.py` to point to the image you want to process.

Example:

```python
image_path = "path_to_your_image.jpg"  # Replace with your image path
```

Then, run the script to generate the caption:

```python
python src/main.py  # Replace with your image path
```

The script will load the image, process it with the BLIP model, and print the generated caption in the terminal.

### 2. Visual Question Answering (VQA)

You can also ask questions about an image by modifying the img_url and question in the script.

#### Example:

```python
img_url = "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"  # Replace with your image URL
question = "What is in the image?"  # Replace with your question
```

Run the script to get an answer to your question based on the image content:

```python
python src/main.py
```

### 3. Expected Output

After running the script, you will see the following:

```bash
Generated Caption: A person standing on a mountain peak with a backpack.
Answer: A person standing on a mountain.
```

This demonstrates the power of multimodal learning, where the model understands both the visual content and the text.

## Contribution

Contributions are always welcome! If you have ideas, suggestions, or improvements, feel free to open an issue or submit a pull request. Please ensure your changes align with the project goals and follow the code of conduct.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.

### Acknowledgments

This project uses third-party libraries and models, including:

- **Hugging Face Transformers Library**: Licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).
- **Salesforce BLIP Model**: Please refer to Salesforce's license and terms of use for this model.

Users of this project are required to comply with the licenses of these third-party components.
