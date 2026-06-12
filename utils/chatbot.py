import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def answer_question(context, question):
    prompt = f"""
    You are a legal assistant.

    Use ONLY the information below to answer the question.

    Legal Content:
    {context}

    Question:
    {question}

    Answer in simple English.
    """

    response = model.generate_content(prompt)
    return response.text