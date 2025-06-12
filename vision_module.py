# from transformers import BlipProcessor, BlipForConditionalGeneration
# from PIL import Image
# import torch

# # Load BLIP model and processor once
# processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# def analyze_dream_image(image_path):
#     try:
#         image = Image.open(image_path).convert('RGB')
#         inputs = processor(image, return_tensors="pt")

#         with torch.no_grad():
#             output = model.generate(**inputs)

#         caption = processor.decode(output[0], skip_special_tokens=True)
#         return f"Dream Image Interpretation: {caption}"

#     except Exception as e:
#         return f"Error analyzing image: {str(e)}"
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
from nlp_module import interpret_dream  # Import your text interpretation logic

# Load BLIP model and processor once
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def analyze_dream_image(image_path):
    try:
        image = Image.open(image_path).convert('RGB')
        inputs = processor(image, return_tensors="pt")

        with torch.no_grad():
            output = model.generate(**inputs)

        caption = processor.decode(output[0], skip_special_tokens=True)

        # Feed the caption to your existing dream interpretation function
        interpretation, symbols, emotion = interpret_dream(caption)

        return f" \n\n Interpretation:\n{interpretation}"

    except Exception as e:
        return f"Error analyzing image: {str(e)}"
