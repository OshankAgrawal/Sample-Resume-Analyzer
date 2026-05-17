from src.components.recommendation_engine import RecommendationEngine

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


engine = RecommendationEngine()

response = engine.generate_recommendation(
    resume_path,
    job_description
)

print("\nFinal AI Recommendation:\n")

print(response)