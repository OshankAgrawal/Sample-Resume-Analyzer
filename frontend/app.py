import streamlit as st
import requests

st.set_page_config(
    page_title="AI Resume Analyzer",
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
            files = {
                "resume": (
                    upload_file.name,
                    upload_file.getvalue(),
                    upload_file.type
                )
            }

            data = {
                "job_description": job_description
            }

            response = requests.post(
                "http://127.0.0.1:8000/analyze-resume",
                files=files,
                data=data
            )

            if response.status_code == 200:

                result = response.json()

                st.success("Analysis completed Successfully!")

                # Scores
                st.subheader("Match Scores")

                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Semantic Score",
                    f"{result["semantic_match_score"]}%"
                )

                col2.metric(
                    "LLM Score",
                    f"{result["llm_match_score"]}%"
                )

                col3.metric(
                    "Final Score",
                    f"{result["final_match_score"]}%"
                )

                # Missing skills
                st.subheader("Missing Skills")

                for item in result["missing_skills"]:
                    st.write(f"- {item}")

                # Stringths
                st.subheader("Strengths")

                for item in result["strengths"]:
                    st.write(f"- {item}")

                # Weaknesses
                st.subheader("Weaknesses")

                for item in result["weaknesses"]:
                    st.write(f"- {item}")

                # Suggestions
                st.subheader("Suggestions")

                for item in result["suggestions"]:
                    st.write(f"- {item}")

                # Recommendation
                st.subheader("Recommendation")

                recommendation = result["recommendation"]

                if recommendation == "Shortlist":
                    st.success(f"{recommendation}")
                else:
                    st.error(f"{recommendation}")

            else:

                st.error("API request failed.")