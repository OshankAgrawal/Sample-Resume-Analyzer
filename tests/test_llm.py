from src.components.resume_parser import ResumeParser
from src.components.llm_analyzer import LLMAnalyzer


# Resume path
resume_path = "Oshank_Agrawal.pdf"

# Sample JD
job_description = """
Looking for a Python Developer with experience in:
- FastAPI
- Machine Learning
- NLP
- LangChain
- SQL
- Docker
"""


# Extract resume text
parser = ResumeParser(resume_path)

resume_text = parser.extract_resume_text()


# Analyze using LLM
analyzer = LLMAnalyzer()

response = analyzer.analyze_resume(
    resume_text=resume_text,
    job_description=job_description
)

print(response)