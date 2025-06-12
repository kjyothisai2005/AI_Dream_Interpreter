import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

def interpret_dream_with_gemini(dream_text):
    prompt = f"""
     Interpret the following dream exclusively from a Jungian analytical psychology perspective.
    Focus solely on core Jungian concepts such as **archetypes**, the **collective unconscious**,
    the process of **individuation**, the **Shadow**, the **Persona**,
    and themes of **transformation** or **self-realization**.
    Provide a concise interpretation, strictly limited to 10-12 lines.

    Dream: {dream_text}

    Provide a detailed Jungian interpretation. Your response should be plain text.
    Do not use any markdown formatting (e.g., headings, bolding, italics, bullet points).
    Do not include an introductory sentence or a conclusion/summary section.
    exclude sexual content.
    """
    response = model.generate_content(prompt)
    return response.text.strip()
