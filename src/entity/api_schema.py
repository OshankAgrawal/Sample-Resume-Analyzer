from pydantic import BaseModel
from typing import List


class AnalysisResponse(BaseModel):

    semantic_match_score: float

    llm_match_score: int

    final_match_score: float

    missing_skills: List[str]

    strengths: List[str]

    weaknesses: List[str]

    suggestions: List[str]

    recommendation: str