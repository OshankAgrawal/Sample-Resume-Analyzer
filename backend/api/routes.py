import os
import shutil
import sys

from fastapi import APIRouter, UploadFile, File, Form

from src.components.recommendation_engine import RecommendationEngine
from src.entity.api_schema import AnalysisResponse
from src.config.app_config import AppConfig

from src.logger.logger import logging
from src.exception.custom_exception import CustomException

router = APIRouter()

UPLOAD_DIR = AppConfig.UPLOAD_DIR

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/")
async def health_check():
    return {
        "status": "OK",
        "message": "AI Resume Analyzer API Running"
    }

@router.post("/analyze-resume", response_model=AnalysisResponse)
async def analyze_resume(resume: UploadFile = File(...), job_description: str = Form(...)):

    try:
        logging.info("Resume analysis API called")

        # Save uploaded file
        file_path = os.path.join(UPLOAD_DIR, resume.filename)

        with open(file_path, "wb") as f:
            shutil.copyfileobj(resume.file, f)

        logging.info(f"Resume saved successfully: {file_path}")

        # Run recommendation engine
        engine = RecommendationEngine()

        response = engine.generate_recommendation(
            resume_path=file_path,
            job_description=job_description
        )

        logging.info("Resume analysis completed successfully")

        if os.path.exists(file_path):
            os.remove(file_path)
            logging.info("Uploaded file deleted forever")

        return response
    
    except Exception as e:
        logging.error("Error occured in analyze_resume API")
        raise CustomException(e, sys)