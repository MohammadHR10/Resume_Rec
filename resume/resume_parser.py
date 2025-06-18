import fitz  # PyMuPDF

def extract_text_from_pdf(path):
    import fitz
    doc = fitz.open(path)
    text = "".join(page.get_text() for page in doc)
    return text[:1000]  # Trim for speed

