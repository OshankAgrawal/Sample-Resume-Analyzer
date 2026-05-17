import streamlit as st
import requests
from config import FrontendConfig
from services.api_service import analyze_resume_api
from utils.ui_helper import display_scores_cards, display_recommendation, display_list_section

st.markdown(
    """
    <style>

    .main {
        padding-top: 2rem;
    }

    .stButton button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-size: 18px;
        font-weight: bold;
    }

    .score-card {
        padding: 20px;
        border-radius: 15px;
        background-color: #262730;
        text-align: center;
        color: white;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }

    .recommendation-box {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: white;
        margin-top: 20px;
    }

    .shortlist {
        background-color: #28a745;
    }

    .reject {
        background-color: #dc3545;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title=FrontendConfig.APP_TITLE,
    page_icon=FrontendConfig.PAGE_ICON,
    layout="wide"
)

# Title
st.markdown(
    """
    <h1 style='text-align: center;'>
        📄 AI Resume Analyzer
    </h1>

    <p style='text-align: center; font-size:18px;'>
        AI Resume Analysis System
    </p>
    """,
    unsafe_allow_html=True
)

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