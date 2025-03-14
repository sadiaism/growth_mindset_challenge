import streamlit as st
from googletrans import Translator

st.title('Language Translation App')
source_text = st.text_input('Enter the text to translate')

languages = {
    "French 🇫🇷": "fr",
    "Spanish 🇪🇸": "es",
    "German 🇩🇪": "de",
    "Chinese 🇨🇳": "zh-cn",
    "Urdu 🇵🇰": "ur",
    "Arabic 🇸🇦": "ar",
    "Hindi 🇮🇳": "hi"
}

target_language = st.selectbox("Select your target language",options=languages)
translate = st.button('Translate')
if translate:
    translator = Translator()
    out = translator.translate(source_text,dest=languages[target_language])
    st.write(out.text)



