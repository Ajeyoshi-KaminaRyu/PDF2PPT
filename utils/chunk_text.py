def chunk_text(text, max_chunk_size=1000):
    return [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
