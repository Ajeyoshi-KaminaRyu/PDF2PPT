import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from core.pdf_parser import extract_text_from_pdf
from core.summarizer import summarize_text
from core.slide_generator import generate_ppt
import os

st.set_page_config(page_title="AI2Slides - Convert PDF to Slides", layout="wide")

# Sidebar
st.sidebar.title("AI2Slides")
st.sidebar.markdown("🧠 *Turn academic PDFs into PowerPoint slides automatically!*")

st.title("📄➡️📊 AI2Slides: Research Paper to PowerPoint")
st.markdown("Upload a research paper (PDF), and get a summarized PowerPoint presentation.")

uploaded_file = st.file_uploader("📂 Upload your PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    full_text = extract_text_from_pdf("temp.pdf")

    tab1, tab2 = st.tabs(["📄 PDF Preview", "📊 Generated Slides"])

    with tab1:
        st.subheader("📃 Extracted Text from PDF")
        st.text_area("", full_text[:2000] + ("..." if len(full_text) > 2000 else ""), height=300)

    with st.spinner("⏳ Summarizing text and generating slides..."):
        slide_data = summarize_text(full_text)

    st.success("✅ Summarization complete. Preview below or download the slides.")

    with tab2:
        for i, (title, content) in enumerate(slide_data):
            st.markdown(f"### {title}")
            st.write(content)

    output_path = generate_ppt(slide_data)

    with open(output_path, "rb") as f:
        st.download_button("📥 Download Your Slides", f, file_name="AI2Slides_Output.pptx")

    st.markdown("---")
    feedback = st.text_input("💬 Got feedback or feature requests?")
    if st.button("Submit Feedback"):
        st.success("🎉 Thanks! We'll use it to improve the app.")

    os.remove("temp.pdf")
    os.remove(output_path)
