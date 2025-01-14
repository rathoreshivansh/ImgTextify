# Install the transformers library
# !pip install transformers Pillow torch torchvision torchaudio
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# IMAGE CAPTIONING EXAMPLE
# Initialize the processor and model from Hugging Face
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load an image
image_path =r"sample_image.jpg"  # Replace with your image path
image = Image.open(image_path)

# Prepare the image
inputs = processor(image, return_tensors="pt")

# Generate captions
outputs = model.generate(**inputs)
caption = processor.decode(outputs[0], skip_special_tokens=True)
print("Generated Caption:", caption)

# VISUAL QUESTION ANSWERING EXAMPLE
# Load BLIP processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

# Image URL
img_url = "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg"
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert("RGB")

# Specify the question you want to ask about the image
question = "What is in the image?"

# Use the processor to prepare inputs for VQA (image + question)
inputs = processor(raw_image, question, return_tensors="pt")

# Generate the answer from the model
out = model.generate(**inputs)
answer = processor.decode(out[0], skip_special_tokens=True)
print(f"Answer: {answer}")
