import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def answer_question(context, question):

    prompt = f"""
    You are a legal assistant.

    Answer the user's question based on the legal content below.

    If the answer exists in the content,
    provide a clear and simple explanation.

    Legal Content:
    {context}

    Question:
    {question}

    Give the answer in simple English.
    """

    response = model.generate_content(prompt)

    return response.text