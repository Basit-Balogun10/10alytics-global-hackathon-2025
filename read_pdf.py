from pypdf import PdfReader

reader = PdfReader("10Alytics 2025 Prep.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)