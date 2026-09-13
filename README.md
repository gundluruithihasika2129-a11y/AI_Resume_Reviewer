# 📄 AI Resume Reviewer

## Project Overview

AI Resume Reviewer is a Python and NLP-based application that analyzes resumes and provides useful feedback to candidates.

The system extracts information from a resume, identifies skills, analyzes education and experience, checks keywords, evaluates ATS compatibility, calculates a resume score, generates feedback, and compares the resume with a job description.

## Features

- PDF Resume Text Extraction
- Text Preprocessing
- Skill Extraction
- Education Extraction
- Experience Analysis
- Project Analysis
- Keyword Analysis
- ATS Compatibility Check
- Resume Scoring out of 100
- Automatic Feedback Generation
- Job Description Matching
- Resume Score Visualization
- Streamlit Web Interface

## Technologies Used

- Python
- NLP / Text Analysis
- PyPDF2
- NLTK
- spaCy
- Pandas
- Scikit-learn
- Matplotlib
- Streamlit

## Project Structure

AI_Resume_Reviewer/

├── app.py  
├── resume_reviewer.py  
├── requirements.txt  
├── README.md  
├── .gitignore  
│  
├── resumes/  
│   └── sample_resume.pdf  
│  
├── output/  
│  
└── screenshots/

## How to Run

### 1. Create virtual environment

```bash
python -m venv venv