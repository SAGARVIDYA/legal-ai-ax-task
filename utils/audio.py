from gtts import gTTS

def generate_audio(text, filename="summary.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    return filename