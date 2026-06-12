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

st.title("⚖️ LegalX AI Knowledge Centre")
st.markdown("AI-Powered Legal Information Assistant")

# -------------------------
# Load legal files
# -------------------------

DATA_FOLDER = "data"

topic_files = {
    "POCSO Act": "pocso.txt",
    "RTI Act": "rti.txt",
    "Cyber Crime Laws": "cybercrime.txt",
    "Consumer Protection Act": "consumer_protection.txt",
    "GST Registration": "gst_registration.txt"
}


def load_content(filename):
    path = os.path.join(DATA_FOLDER, filename)

    if not os.path.exists(path):
        return "File not found."

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


# -------------------------
# Sidebar
# -------------------------

st.sidebar.title("Legal Topics")

selected_topic = st.sidebar.selectbox(
    "Choose a topic",
    list(topic_files.keys())
)

content = load_content(topic_files[selected_topic])

# -------------------------
# Topic Section
# -------------------------

st.header(selected_topic)

st.subheader("Source Content")

with st.expander("View Legal Content"):
    st.write(content)

# -------------------------
# Summary
# -------------------------

if st.button("Generate Summary"):

    with st.spinner("Generating summary..."):

        summary = generate_summary(content)

        st.session_state["summary"] = summary

    st.subheader("📄 Summary")
    st.write(summary)

# Show saved summary

if "summary" in st.session_state:

    st.subheader("📄 Summary")
    st.write(st.session_state["summary"])

# -------------------------
# Key Information
# -------------------------

if st.button("Extract Key Information"):

    with st.spinner("Extracting key information..."):

        info = extract_key_info(content)

        st.session_state["info"] = info

if "info" in st.session_state:

    st.subheader("🔍 Key Information")
    st.write(st.session_state["info"])

# -------------------------
# Audio Summary
# -------------------------

if "summary" in st.session_state:

    st.subheader("🔊 Audio Summary")

    audio_file = generate_audio(
        st.session_state["summary"]
    )

    st.audio(audio_file)

# -------------------------
# AI Legal Assistant
# -------------------------

st.subheader("🤖 AI Legal Assistant")

question = st.text_input(
    "Ask a question about this topic"
)

if st.button("Ask Question"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Thinking..."):

            answer = answer_question(
                content,
                question
            )

        st.success(answer)

# -------------------------
# Footer
# -------------------------

st.markdown("---")
st.caption(
    "Built for LegalX AI/ML Internship Assessment"
)