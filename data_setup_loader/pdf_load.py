import fitz  # PyMuPDF
import pandas as pd

pdf_path = "ML_Engineer_Manuar.pdf"

texts = []
doc = fitz.open(pdf_path)

for page in doc:
    text = page.get_text()
    texts.append(text)

print(texts)

#docx file load, json

doc.close()


