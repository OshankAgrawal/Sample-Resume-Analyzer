import sys

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from src.logger.logger import logging
from src.exception.custom_exception import CustomException

class SimilarityEngine:
    """
        Handles semantic similarity calculation
        between resume and job description
    """

    def __init__(self):
        
        try:
            logging.info("Loading sentence transformer model")

            self.model = SentenceTransformer(
                "sentence-transformers/all-MiniLM-L6-v2"
            )

            logging.info("Model loaded successfully")

        except Exception as e:
            logging.error("Error loading embedding model")
            raise CustomException(e, sys)
        

    def calculate_similarity(self, resume_text: str, job_description: str) -> float:
        try:
            logging.info("Entered similarity calculation method")

            # Generate embeddings
            resume_embeddings = self.model.encode([resume_text])

            jd_embeddings = self.model.encode([job_description])

            # Calculate cosine similarity
            similarity_score = cosine_similarity(
                resume_embeddings,
                jd_embeddings
            )[0][0]

            # Convert score into percentage
            similarity_percentage = round(float(similarity_score * 100), 2)

            logging.info(f"Similarity score claculated: {similarity_percentage}")

            return similarity_percentage
        
        except Exception as e:
            logging.error("Error during similarity calculation")
            raise CustomException(e, sys)