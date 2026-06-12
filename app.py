import streamlit as st
import os

from utils.summarizer import generate_summary
from utils.extractor import extract_key_info
from utils.audio import generate_audio
from utils.chatbot import answer_question

st.set_page_config(
    page_title="LegalX AI Knowledge Centre",
    page_icon="⚖️",
    layout="wide"
)

# --------------------------
# Load Topic Files
# --------------------------

TOPICS = {
    "POCSO Act": "data/pocso.txt",
    "RTI Act": "data/rti.txt",
    "Cyber Crime Laws": "data/cybercrime.txt",
    "Consumer Protection Act": "data/consumer_protection.txt",
    "GST Registration": "data/gst_registration.txt"
}


def load_content(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error loading file: {e}"


# --------------------------
# UI
# --------------------------

st.title("⚖️ LegalX AI Knowledge Centre")
st.markdown(
    "AI-powered legal knowledge platform for simplified legal information."
)

# Sidebar

st.sidebar.title("Legal Topics")

selected_topic = st.sidebar.selectbox(
    "Choose a topic",
    list(TOPICS.keys())
)

content = load_content(TOPICS[selected_topic])

# --------------------------
# Topic Content
# --------------------------

st.header(selected_topic)

with st.expander("📄 View Source Content"):
    st.write(content)

# --------------------------
# Summary
# --------------------------

col1, col2 = st.columns(2)

with col1:

    if st.button("Generate Summary"):

        try:

            with st.spinner("Generating summary..."):

                summary = generate_summary(content)

                st.session_state["summary"] = summary

        except Exception as e:

            st.error(f"Summary Error: {e}")

# Display Summary

if "summary" in st.session_state:

    st.subheader("📋 Summary")

    st.write(st.session_state["summary"])

# --------------------------
# Key Information
# --------------------------

with col2:

    if st.button("Extract Key Information"):

        try:

            with st.spinner("Extracting information..."):

                info = extract_key_info(content)

                st.session_state["info"] = info

        except Exception as e:

            st.error(f"Extraction Error: {e}")

if "info" in st.session_state:

    st.subheader("🔍 Key Information")

    st.write(st.session_state["info"])

# --------------------------
# Audio
# --------------------------

if "summary" in st.session_state:

    st.subheader("🔊 Audio Summary")

    try:

        audio_file = generate_audio(
            st.session_state["summary"]
        )

        st.audio(audio_file)

    except Exception as e:

        st.error(f"Audio Error: {e}")

# --------------------------
# AI Legal Assistant
# --------------------------

st.subheader("🤖 AI Legal Assistant")

question = st.text_input(
    "Ask a question about this topic"
)

if st.button("Ask Question"):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        try:

            with st.spinner("Thinking..."):

                answer = answer_question(
                    content,
                    question
                )

            st.success(answer)

        except Exception as e:

            st.error(f"Chatbot Error: {e}")

# --------------------------
# Footer
# --------------------------

st.markdown("---")

st.caption(
    "Built for LegalX AI/ML Internship Assessment"
)