# # SYMBOL_DB = {
# #     "water": "Symbolizes deep unconscious thoughts (Freud).",
# #     "snake": "Represents primal instincts or transformation (Jung).",
# #     "teeth": "Fear of change or aging (Freud).",
# #     "falling": "Loss of control or anxiety (Freud).",
# #     "mother": "Anima archetype, nurturing force (Jung).",
# #     "mirror": "Self-reflection and persona (Jung)."
# # }

# # def interpret_dream(text):
# #     found = [symbol for symbol in SYMBOL_DB if symbol in text.lower()]
# #     if found:
# #         return " | ".join([f"{symbol}: {SYMBOL_DB[symbol]}" for symbol in found])
# #     return "Could not match known symbols. Consider elaborating your dream."
# SYMBOL_DB = {
#     "water": "Symbolizes deep unconscious thoughts (Freud).",
#     "snake": "Represents primal instincts or transformation (Jung).",
#     "teeth": "Fear of change or aging (Freud).",
#     "falling": "Loss of control or anxiety (Freud).",
#     "mother": "Anima archetype, nurturing force (Jung).",
#     "mirror": "Self-reflection and persona (Jung)."
# }

# def interpret_dream(text):
#     found = [symbol for symbol in SYMBOL_DB if symbol in text.lower()]
#     if found:
#         return " | ".join([f"{symbol}: {SYMBOL_DB[symbol]}" for symbol in found])
#     return "Could not match known symbols. Consider elaborating your dream."

# def analyze_dream_image(image_path):
#     # Placeholder logic – replace with actual model or API call
#     # For now, return a fake symbolic interpretation based on "vision"
#     import random
#     mock_symbols = list(SYMBOL_DB.keys())
#     selected = random.sample(mock_symbols, k=2)
#     return " | ".join([f"{s}: {SYMBOL_DB[s]}" for s in selected])
import torch
import clip
from PIL import Image

# Expanded symbolic database
SYMBOL_DB = {
    "water": "Symbolizes deep unconscious thoughts (Freud).",
    "snake": "Represents primal instincts or transformation (Jung).",
    "teeth": "Fear of change or aging (Freud).",
    "falling": "Loss of control or anxiety (Freud).",
    "mother": "Anima archetype, nurturing force (Jung).",
    "mirror": "Self-reflection and persona (Jung).",
    "fire": "Transformation or emotional intensity (Jung).",
    "cage": "Feeling trapped or constrained (Freud).",
    "flight": "Desire for escape or freedom (Jung).",
    "shadow": "Repressed aspects of self (Jung)."
}

device = "cuda" if torch.cuda.is_available() else "cpu"
clip_model, preprocess = clip.load("ViT-B/32", device=device)

def interpret_dream(text):
    found = [symbol for symbol in SYMBOL_DB if symbol in text.lower()]
    if found:
        return " | ".join([f"{symbol}: {SYMBOL_DB[symbol]}" for symbol in found])
    return "Could not match known symbols. Consider elaborating your dream."

def analyze_dream_image(image_path):
    image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)

    # Create text prompts for each symbol
    prompts = [f"A picture of {symbol}" for symbol in SYMBOL_DB]
    text_tokens = clip.tokenize(prompts).to(device)

    with torch.no_grad():
        image_features = clip_model.encode_image(image)
        text_features = clip_model.encode_text(text_tokens)

        # Normalize
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        similarities = (image_features @ text_features.T).squeeze(0)
        top_indices = similarities.topk(3).indices.tolist()

    matched = [list(SYMBOL_DB.keys())[i] for i in top_indices]
    return " | ".join([f"{symbol}: {SYMBOL_DB[symbol]}" for symbol in matched])
