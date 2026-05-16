from src.components.resume_parser import ResumeParser

file_path = "oshankagrawal.docx"

parser = ResumeParser(file_path)

text = parser.extract_resume_text()

print(text)