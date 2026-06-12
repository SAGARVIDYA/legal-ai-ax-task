# ⚖️ LegalX AI Knowledge Centre

## Project Overview

LegalX AI Knowledge Centre is an AI-powered legal information platform designed to make legal knowledge simple, accessible, and user-friendly.

The application automatically processes legal content and provides:

* AI-generated summaries
* Key information extraction
* Audio explanations
* Legal question answering
* Topic-based legal knowledge cards

The system helps users understand legal concepts without requiring legal expertise.

---

## Features

### 1. Legal Knowledge Topics

The application currently supports:

* POCSO Act
* Right to Information (RTI) Act
* Cyber Crime Laws
* Consumer Protection Act
* GST Registration

---

### 2. AI-Generated Summary

The system automatically generates:

* Simple language summaries
* Easy-to-understand explanations
* User-friendly legal information

Powered by Google Gemini AI.

---

### 3. Key Information Extraction

The application extracts:

* Key Rights
* Important Provisions
* Important Penalties
* Who Can Benefit

from the legal content automatically.

---

### 4. AI Legal Assistant

Users can ask questions related to the selected legal topic.

Examples:

* What is RTI?
* Who can file an RTI request?
* What is the POCSO Act?
* What are consumer rights?
* Who needs GST Registration?

The assistant provides context-aware answers based on the selected legal content.

---

### 5. Audio Summary

Generated summaries are converted into speech using Google Text-to-Speech (gTTS).

Features:

* Play audio summary
* Improve accessibility
* User-friendly listening experience

---

## Architecture

```text
Legal Content Files (.txt)
            │
            ▼
      Gemini AI
            │
 ┌──────────┼──────────┐
 ▼          ▼          ▼
Summary   Extraction  Q&A
            │
            ▼
      Audio Generation
            │
            ▼
       Streamlit UI
```

---

## Technologies Used

### Frontend

* Streamlit

### AI Model

* Google Gemini 2.5 Flash

### Backend

* Python

### Audio Processing

* Google Text-to-Speech (gTTS)

### Environment Management

* Python Dotenv

---

## Project Structure

```text
legal-ai-ax-task/

│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── pocso.txt
│   ├── rti.txt
│   ├── cybercrime.txt
│   ├── consumer_protection.txt
│   └── gst_registration.txt
│
└── utils/
    ├── summarizer.py
    ├── extractor.py
    ├── chatbot.py
    └── audio.py
```

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
cd legal-ai-ax-task
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
```

### Run Application

```bash
streamlit run app.py
```

---

## Automation Pipeline

The application follows an automated AI workflow:

```text
Legal Content
      │
      ▼
AI Processing
      │
      ▼
Summary Generation
      │
      ▼
Information Extraction
      │
      ▼
Audio Generation
      │
      ▼
Question Answering
      │
      ▼
Knowledge Centre Interface
```

---

## Challenges Faced

* Simplifying legal content into understandable language.
* Extracting structured information from legal documents.
* Integrating AI-generated summaries and question answering.
* Implementing audio generation for accessibility.

---

## Future Improvements

* RAG (Retrieval-Augmented Generation)
* FAISS Vector Database Integration
* Source Citations
* Chat History
* Multi-language Support
* Speech-to-Text
* Authentication System
* Legal Document Upload Feature

---

## Conclusion

This project demonstrates the use of Generative AI for legal knowledge automation. By combining Google Gemini, Streamlit, and Text-to-Speech technologies, the application provides an interactive and user-friendly platform for understanding legal information.

---

### Developed for

**LegalX AI/ML Internship – Round 2 Assessment**
