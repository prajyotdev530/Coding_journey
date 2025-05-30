import fitz  # PyMuPDF
from transformers import pipeline

ner = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(text):
    entities = ner(text)
    return [e["word"] for e in entities if e["entity_group"] == "MISC"]