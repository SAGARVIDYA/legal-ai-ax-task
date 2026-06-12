import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_summary(text):
    prompt = f"""
    Summarize the following legal content in simple English.
    Maximum 250 words.

    {text}
    """

    response = model.generate_content(prompt)
    return response.text