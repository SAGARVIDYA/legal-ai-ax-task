import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_key_info(text):
    prompt = f"""
    Extract the following information from the legal content.

    1. Key Rights
    2. Important Provisions
    3. Important Penalties
    4. Who Can Benefit

    Format the output clearly with headings.

    Legal Content:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text