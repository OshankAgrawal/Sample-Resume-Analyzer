# AI Resume Analyzer

A simple AI-based Resume Analyzer that compares a candidate's resume with a job description and provides useful insights like match score, missing skills, strengths, weaknesses, and improvement suggestions.

---

## Features

* Upload Resume in PDF or DOCX format
* Compare Resume with Job Description
* Semantic Similarity Matching
* AI-Based Resume Analysis
* Missing Skills Detection
* Strengths & Weaknesses Analysis
* Final Recommendation System
* Interactive Streamlit UI

---

## Technologies Used

#### Backend
* Python
* FastAPI
* LangChain
* Groq API
* SentenceTransformers
* Scikit-learn

#### Frontend
* Streamlit

#### Other Libraries
* PyMuPDF
* python-docx
* Pydantic

---

## Project Structure

```bash
Resume-Analyzer/
 │
 ├── api/
 ├── frontend/
 ├── src/
 │    ├── components/
 │    ├── config/
 │    ├── entity/ 
 │    ├── exception/ 
 │    ├── logger/ 
 │    ├── prompt/ 
 │    └── utils/ 
 │
 ├── tests/ 
 ├── app.py 
 ├── requirements.txt 
 ├── setup.py 
 └── README.md
```

---

## How It Works

1. User uploads a resume.
2. User enters/pastes the Job Description.
3. The system extracts resume text.
4. Skills are extracted using NLP techniques.
5. Resume skills are compared with JD skills.
6. A final score is generated.
7. Recommendations and missing skills are displayed.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/OshankAgrawal/Resume-Analyzer.git
cd Resume-Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

---

## Environment Variables

Create a `.env` file in the root directory and add:

```bash
GROQ_API_KEY=your_api_key
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn app:app --reload
```

Backend will run on: `http://127.0.0.1:8000`

---

## Run Frontend

```bash
streamlit run frontend/app.py
```

Frontend will run on: `http://localhost:8501`

---

## API Endpoint

### Analyze Resume

`POST /analyze-resume`

#### Input
* Resume File
* Job Description

#### Output
* Semantic Match Score
* LLM Match Score
* Final Match Score
* Missing Skills
* Strengths
* Weaknesses
* Suggestions
* Recommendation

---

## Sample Workflow

* Upload Resume PDF
* Paste Job Description
* Click Analyze
* View:

  * Resume Score
  * Skill Match Percentage
  * Missing Skills
  * Recommendations

---

## Future Improvements

* Multi Resume Analysis
* Resume Ranking System
* Authentication
* Database Integration
* Dashboard Analytics

---

##  Author

**Oshank Agrawal**
*Developer, Problem Solver, Tech Enthusiast*
🔗 [LinkedIn](https://www.linkedin.com/in/oshankagrawal/) • 📧 [E-Mail](mailto:oshankagrawal@gmail.com)
