import sys
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

from src.config.configuration import GROQ_API_KEY
from src.prompt.prompts import ANALYSIS_PROMPT
from src.logger.logger import logging
from src.exception.custom_exception import CustomException
from src.utils.json_parser import extract_json
from src.entity.response_schema import ResumeAnalysisResponse

class LLMAnalyzer:
    """Handles LLM-based resume analysis"""

    def __init__(self):
        
        self.llm = ChatGroq(
            groq_api_key = GROQ_API_KEY,
            model="llama-3.1-8b-instant"
        )

    
    def analyze_resume(
            self,
            resume_text: str,
            job_description: str
    ):
        try:
            logging.info("Entered LLM analysis pipeline")

            prompt = PromptTemplate(
                input_variables = [
                    "resme_text",
                    "job_description"
                ],
                template = ANALYSIS_PROMPT
            )

            formatted_prompt = prompt.format(
                resume_text=resume_text,
                job_description=job_description
            )

            response = self.llm.invoke(formatted_prompt)

            logging.info("LLM analysis completed successfully")

            parsed_response = extract_json(response.content)

            validate_response = ResumeAnalysisResponse(**parsed_response)

            return validate_response.dict()

        except Exception as e:
            logging.error("Error occurred during LLM analysis")
            raise CustomException(e, sys)