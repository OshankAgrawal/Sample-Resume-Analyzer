import os

class AppConfig:

    # Upload Directory
    UPLOAD_DIR = "artifacts"

    # Embedding Model
    EMBEDDING_MODEL = ("sentence-transformers/all-MiniLM-L6-v2")

    # LLM Model
    LLM_MODEL = "llama-3.1-8b-instant"

    # Similarity Threshold
    SIMILARITY_THRESHOLD = 60

    # Allowed Extensions
    ALLOWED_EXTENSIONS = [".pdf", ".docx"]

    # API Metadata
    API_TITLE = "AI Resume Analyzer"

    API_VERSION = "1.0"

    API_DESCRIPTION = ("Production Grade AI Resume Analysis System")