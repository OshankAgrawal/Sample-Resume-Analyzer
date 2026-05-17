from src.components.resume_parser import ResumeParser
from src.components.similarity_engine import SimilarityEngine


resume_path = "Oshank_Agrawal.pdf"

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

# Similarity calculation
similarity_engine = SimilarityEngine()

score = similarity_engine.calculate_similarity(
    resume_text,
    job_description
)

print(f"\nSemantic Similarity Score: {score}%")