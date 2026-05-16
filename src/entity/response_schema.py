from pydantic import BaseModel
from typing import List

class ResumeAnalysisResponse(BaseModel):

    match_percentage: int

    missing_skills: List[str]

    strengths: List[str]

    weaknesses: List[str]

    suggestions: List[str]

    recommendation: str