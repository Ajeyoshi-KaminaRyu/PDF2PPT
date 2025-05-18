from transformers import pipeline
from utils.chunk_text import chunk_text

def summarize_text(text):
    summarizer = pipeline("summarization", model="t5-small")
    chunks = chunk_text(text, max_chunk_size=1000)
    slide_data = []
    for i, chunk in enumerate(chunks[:10]):
        summary = summarizer(chunk, max_length=80, min_length=30, do_sample=False)[0]['summary_text']
        slide_data.append((f"Slide {i+1}", summary))
    return slide_data