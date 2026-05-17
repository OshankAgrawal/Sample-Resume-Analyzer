import requests
from config import FrontendConfig

def analyze_resume_api(uploaded_files, job_description):
    """Calls FastAPI backend"""

    files = {
        "resume": (
            uploaded_files.name,
            uploaded_files.getvalue(),
            uploaded_files.type
        )
    }

    data = {
        "job_description": job_description
    }

    response = requests.post(
        FrontendConfig.ANALYZE_ENDPOINT,
        files=files,
        data=data
    )

    return response