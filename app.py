import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Chinese Flashcards",
    page_icon="🀄",
    layout="wide"
)

html_path = Path("chinese_flashcards_from_your_pdf.html")

if html_path.exists():
    html = html_path.read_text(encoding="utf-8")
    components.html(html, height=1100, scrolling=True)
else:
    st.error("Could not find chinese_flashcards_from_your_pdf.html")
