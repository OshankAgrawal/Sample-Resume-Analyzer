ANALYSIS_PROMPT ="""
    You are an advanced AI Resume Analyzer.

    Analyze the provided resume against the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Return ONLY valid JSON in the following format:

    {{
        "match_percentage": integer,
        "missing_skills": [],
        "strengths": [],
        "weaknesses": [],
        "suggestions": [],
        "Recommendations": "Shortlist or Reject"
    }}

    Rules:
        - Match percentage should be realistic.
        - Suggestion should be actionable.
        - Missing skills should be relevant to the job description.
        - Return STRICT JSON only.
"""