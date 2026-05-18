class FrontendConfig:

    API_BASE_URL = "http://backend:8000"

    ANALYZE_ENDPOINT = (
        f"{API_BASE_URL}/analyze-resume"
    )

    APP_TITLE = "AI Resume Analyzer"

    PAGE_ICON = "📄"