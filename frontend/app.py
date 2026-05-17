import streamlit as st
import requests
from config import FrontendConfig
from services.api_service import analyze_resume_api
from utils.ui_helper import display_scores_cards, display_recommendation, display_list_section

st.set_page_config(
    page_title=FrontendConfig.APP_TITLE,
    page_icon=FrontendConfig.PAGE_ICON,
    layout="wide"
)

# Title
st.title("AI Resume Analyzer")

st.markdown(
    """
    Analyze resumes intelligently using:
    - Semantic Similarity
    - LLM Analysis
    - Hybrid AI Scoring
    """
)

# Sidebar
st.sidebar.header("About")

st.sidebar.info(
    """
    AI Resume Analyzer built using:

    - FastAPI
    - Langchain
    - Groq
    - SentenceTransformers
    """
)

# Upload Resume
upload_file = st.file_uploader(
    "Upload Resume",
    type = ["pdf", "docx"]
)

# Job Description
job_description = st.text_area(
    "Paste Job Description",
    height=250
)

# Analyze Button
if st.button("Analyze Resume"):

    if upload_file is None:

        st.warning("Please upload a resume.")

    elif not job_description.strip():

        st.warning("Please enter job description.")

    else:

        with st.spinner("Analyzing Resume..."):
            response = analyze_resume_api(upload_file, job_description)

            if response.status_code == 200:

                result = response.json()

                st.success("Analysis completed Successfully!")

                # Scores
                display_scores_cards(result)

                # Missing skills
                display_list_section("Missing Skills", result["missing_skills"])

                # Strengths
                display_list_section("Strengths", result["strengths"])

                # Weaknesses
                display_list_section("Weaknesses", result["weaknesses"])

                # Suggestions
                display_list_section("Suggestions", result["suggestions"])

                # Recommendation
                display_recommendation(result)

            else:

                st.error("API request failed.")