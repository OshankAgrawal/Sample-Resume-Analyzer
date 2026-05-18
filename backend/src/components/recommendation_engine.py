import sys
from src.logger.logger import logging
from src.exception.custom_exception import CustomException

from src.components.resume_parser import ResumeParser
from src.components.similarity_engine import SimilarityEngine
from src.components.llm_analyzer import LLMAnalyzer


class RecommendationEngine:
    """Main AI Resume Recommendation Pipeline"""

    def __init__(self):
        
        self.similarity_engine = SimilarityEngine()

        self.llm_analyzer = LLMAnalyzer()


    def generate_recommendation(self, resume_path: str, job_description: str):

        try:
            logging.info("Entered recommendation pipeline")

            # Step 1: Extract Resume Text
            parser = ResumeParser(resume_path)

            resume_text = parser.extract_resume_text()

            logging.info("Resume text extracted successfully")

            # Step 2: Semantic Similarity
            semantic_score = (self.similarity_engine.calculate_similarity(
                resume_text,
                job_description
            ))

            logging.info(f"Semantic similarity score: {semantic_score}")

            # Step 3: LLM Analysis
            llm_response = (self.llm_analyzer.analyze_resume(
                resume_text,
                job_description
            ))

            logging.info("LLM analysis completed")

            # Step 4: Hybrid Final Score
            llm_match_score = llm_response["match_percentage"]

            final_match_score = round(
                (semantic_score + llm_match_score) / 2,
                2
            )

            logging.info(f"Final Hybrid score: {final_match_score}")

            # Final Recommendation Logic
            if final_match_score >= 75:
                recommendation = "Shortlist"

            elif final_match_score >= 60:
                recommendation = "Hold"

            else:
                recommendation = "Reject"

            # Step 5: Final Response
            final_response = {
                "semantic_match_score": semantic_score,
                "llm_match_score": llm_match_score,
                "final_match_score": final_match_score,

                "missing_skills": llm_response["missing_skills"],
                "strengths": llm_response["strengths"],
                "weaknesses": llm_response["weaknesses"],
                "suggestions": llm_response["suggestions"],
                "recommendation": recommendation
            }

            logging.info("Recommendation pipeline completed successfully")

            return final_response
        
        except Exception as e:
            logging.error("Error occured in recommendation pipeline")
            raise CustomException(e, sys)