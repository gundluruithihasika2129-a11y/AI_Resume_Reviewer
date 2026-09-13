from PyPDF2 import PdfReader
import re


# ==========================================
# STEP 6: PDF RESUME TEXT EXTRACTION
# ==========================================

def extract_text_from_pdf(file):
    """
    Extract text from all pages of a PDF resume.

    Parameters:
        file: Uploaded PDF file

    Returns:
        str: Extracted resume text
    """

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


# ==========================================
# STEP 7: TEXT PREPROCESSING
# ==========================================

def preprocess_text(text):
    """
    Clean and normalize resume text.

    Parameters:
        text: Raw resume text

    Returns:
        str: Cleaned resume text
    """

    # Convert text to lowercase
    text = text.lower()

    # Replace multiple spaces/new lines with one space
    text = re.sub(r"\s+", " ", text)

    # Remove unnecessary special characters
    # Keep letters, numbers, +, #, ., -, and spaces
    text = re.sub(
        r"[^a-zA-Z0-9+#.\- ]",
        " ",
        text
    )

    # Remove extra spaces from beginning/end
    return text.strip()


# ==========================================
# STEP 8: SKILL EXTRACTION
# ==========================================

# List of important technical skills
SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "power bi",
    "tableau",
    "excel",
    "statistics",
    "data visualization",
    "matplotlib",
    "seaborn",
    "keras",
    "flask",
    "django",
    "git",
    "github"
]


def extract_skills(text):
    """
    Find technical skills mentioned in the resume.

    Parameters:
        text: Resume text

    Returns:
        list: Detected technical skills
    """

    # Convert resume text to lowercase
    text = text.lower()

    # Store detected skills
    found_skills = []

    # Check every skill in the skills list
    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return found_skills
# ==========================================
# STEP 9: EDUCATION EXTRACTION
# ==========================================

# Common education keywords
EDUCATION_KEYWORDS = [
    "b.tech",
    "b.e",
    "b.sc",
    "bca",
    "bba",
    "m.tech",
    "m.e",
    "m.sc",
    "mca",
    "mba",
    "bachelor",
    "master",
    "degree",
    "computer science",
    "information technology",
    "engineering",
    "university",
    "college"
]


def extract_education(text):
    """
    Find education-related information
    mentioned in the resume.

    Parameters:
        text: Resume text

    Returns:
        list: Detected education keywords
    """

    # Convert resume text to lowercase
    text = text.lower()

    # Store detected education information
    found_education = []

    # Check every education keyword
    for keyword in EDUCATION_KEYWORDS:

        if keyword in text:
            found_education.append(keyword)

    return found_education
# ==========================================
# STEP 10: EXPERIENCE ANALYSIS
# ==========================================

# Common experience-related keywords
EXPERIENCE_KEYWORDS = [
    "experience",
    "work experience",
    "internship",
    "intern",
    "employment",
    "worked",
    "working",
    "developer",
    "software engineer",
    "data analyst",
    "data scientist",
    "machine learning engineer",
    "web developer",
    "python developer",
    "project intern",
    "data science intern"
]


def analyze_experience(text):
    """
    Find work experience and internship-related
    information in the resume.

    Parameters:
        text: Resume text

    Returns:
        list: Detected experience keywords
    """

    # Convert resume text to lowercase
    text = text.lower()

    # Store detected experience information
    found_experience = []

    # Check each experience keyword
    for keyword in EXPERIENCE_KEYWORDS:

        if keyword in text:
            found_experience.append(keyword)

    return found_experience
# ==========================================
# STEP 11: PROJECT ANALYSIS
# ==========================================

# Common project-related keywords
PROJECT_KEYWORDS = [
    "project",
    "projects",
    "developed",
    "developed a",
    "built",
    "built a",
    "created",
    "implemented",
    "designed",
    "application",
    "system",
    "website",
    "model",
    "dashboard"
]


def analyze_projects(text):
    """
    Find project-related information in the resume.

    Parameters:
        text: Resume text

    Returns:
        list: Detected project keywords
    """

    # Convert resume text to lowercase
    text = text.lower()

    # Store detected project information
    found_projects = []

    # Check each project keyword
    for keyword in PROJECT_KEYWORDS:

        if keyword in text:
            found_projects.append(keyword)

    return found_projects
# ==========================================
# STEP 12: KEYWORD ANALYSIS
# ==========================================

# Important keywords for a Data Science resume
JOB_KEYWORDS = [
    "python",
    "sql",
    "machine learning",
    "data analysis",
    "statistics",
    "pandas",
    "numpy",
    "scikit-learn",
    "data visualization",
    "nlp",
    "deep learning",
    "tensorflow",
    "pytorch",
    "matplotlib",
    "power bi",
    "tableau",
    "excel"
]


def keyword_analysis(text):
    """
    Check important job-related keywords
    present in the resume.

    Parameters:
        text: Resume text

    Returns:
        tuple: Found keywords, missing keywords,
               and keyword match percentage
    """

    # Convert resume text to lowercase
    text = text.lower()

    # Lists to store results
    found_keywords = []
    missing_keywords = []

    # Check every job keyword
    for keyword in JOB_KEYWORDS:

        if keyword in text:
            found_keywords.append(keyword)

        else:
            missing_keywords.append(keyword)

    # Calculate keyword match percentage
    total_keywords = len(JOB_KEYWORDS)

    if total_keywords > 0:
        match_percentage = (
            len(found_keywords) / total_keywords
        ) * 100
    else:
        match_percentage = 0

    return (
        found_keywords,
        missing_keywords,
        round(match_percentage, 2)
    )
# ==========================================
# STEP 13: ATS COMPATIBILITY CHECK
# ==========================================

ATS_SECTION_KEYWORDS = {
    "skills": [
        "skills",
        "technical skills",
        "technical skill"
    ],

    "education": [
        "education",
        "academic background"
    ],

    "experience": [
        "experience",
        "work experience",
        "internship"
    ],

    "projects": [
        "projects",
        "project"
    ],

    "certifications": [
        "certifications",
        "certification",
        "courses"
    ]
}


def ats_check(text):
    """
    Check basic ATS compatibility of a resume.
    """

    text_lower = text.lower()

    found_sections = []
    missing_sections = []

    # Check resume sections
    for section, keywords in ATS_SECTION_KEYWORDS.items():

        if any(keyword in text_lower for keyword in keywords):
            found_sections.append(section)
        else:
            missing_sections.append(section)

    # Check email address
    email_found = bool(
        re.search(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
            text
        )
    )

    # Check phone number
    phone_found = bool(
        re.search(
            r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\d{10}|\d{3}[-.\s]\d{3}[-.\s]\d{4})\b",
            text
        )
    )

    # Calculate ATS score
    score = 0

    # Section score = 70 marks
    score += (
        len(found_sections)
        / len(ATS_SECTION_KEYWORDS)
    ) * 70

    # Email = 15 marks
    if email_found:
        score += 15

    # Phone = 15 marks
    if phone_found:
        score += 15

    return {
        "score": round(score, 2),
        "found_sections": found_sections,
        "missing_sections": missing_sections,
        "email_found": email_found,
        "phone_found": phone_found
    }
# ==========================================
# STEP 14: RESUME SCORING
# ==========================================

def calculate_resume_score(
    skills,
    experience,
    education,
    projects,
    keyword_percentage,
    ats_score
):
    """
    Calculate the overall resume score out of 100.

    Parameters:
        skills: List of detected skills
        experience: List of experience keywords
        education: List of education keywords
        projects: List of project keywords
        keyword_percentage: Keyword match percentage
        ats_score: ATS compatibility score

    Returns:
        dict: Score details and overall score
    """

    # -------------------------------
    # 1. Skills Score - 25 marks
    # -------------------------------

    skill_score = min((len(skills) / 10) * 25, 25)


    # -------------------------------
    # 2. Experience Score - 20 marks
    # -------------------------------

    if len(experience) >= 5:
        experience_score = 20
    elif len(experience) >= 3:
        experience_score = 15
    elif len(experience) >= 1:
        experience_score = 10
    else:
        experience_score = 0


    # -------------------------------
    # 3. Education Score - 15 marks
    # -------------------------------

    if len(education) >= 3:
        education_score = 15
    elif len(education) >= 1:
        education_score = 10
    else:
        education_score = 0


    # -------------------------------
    # 4. Projects Score - 15 marks
    # -------------------------------

    if len(projects) >= 5:
        project_score = 15
    elif len(projects) >= 3:
        project_score = 12
    elif len(projects) >= 1:
        project_score = 8
    else:
        project_score = 0


    # -------------------------------
    # 5. Keyword Score - 10 marks
    # -------------------------------

    keyword_score = min(
        (keyword_percentage / 100) * 10,
        10
    )


    # -------------------------------
    # 6. ATS Score - 10 marks
    # -------------------------------

    ats_score_weighted = min(
        (ats_score / 100) * 10,
        10
    )


    # -------------------------------
    # 7. Completeness Score - 5 marks
    # -------------------------------

    completeness_score = 0

    if len(skills) > 0:
        completeness_score += 1

    if len(experience) > 0:
        completeness_score += 1

    if len(education) > 0:
        completeness_score += 1

    if len(projects) > 0:
        completeness_score += 1

    if keyword_percentage > 0:
        completeness_score += 1


    # -------------------------------
    # Overall Score
    # -------------------------------

    overall_score = (
        skill_score
        + experience_score
        + education_score
        + project_score
        + keyword_score
        + ats_score_weighted
        + completeness_score
    )

    return {
        "skills_score": round(skill_score, 2),
        "experience_score": round(experience_score, 2),
        "education_score": round(education_score, 2),
        "project_score": round(project_score, 2),
        "keyword_score": round(keyword_score, 2),
        "ats_score": round(ats_score_weighted, 2),
        "completeness_score": round(completeness_score, 2),
        "overall_score": round(overall_score, 2)
    }
# ==========================================
# STEP 15: FEEDBACK GENERATION
# ==========================================

def generate_feedback(
    skills,
    experience,
    education,
    projects,
    found_keywords,
    missing_keywords,
    ats_result,
    overall_score
):
    """
    Generate feedback and suggestions
    based on resume analysis.
    """

    feedback = []

    # --------------------------------------
    # 1. Skills Feedback
    # --------------------------------------

    if len(skills) >= 5:
        feedback.append(
            "Good! Your resume contains a good number of technical skills."
        )
    else:
        feedback.append(
            "Improve your resume by adding more relevant technical skills."
        )


    # --------------------------------------
    # 2. Experience Feedback
    # --------------------------------------

    if len(experience) >= 3:
        feedback.append(
            "Good! Your resume contains experience or internship information."
        )
    else:
        feedback.append(
            "Add more details about your internships, work experience, or practical experience."
        )


    # --------------------------------------
    # 3. Education Feedback
    # --------------------------------------

    if len(education) >= 1:
        feedback.append(
            "Good! Education information is present in your resume."
        )
    else:
        feedback.append(
            "Add your educational qualifications clearly."
        )


    # --------------------------------------
    # 4. Project Feedback
    # --------------------------------------

    if len(projects) >= 3:
        feedback.append(
            "Good! Your resume contains project-related information."
        )
    else:
        feedback.append(
            "Add more projects and briefly explain the technologies used."
        )


    # --------------------------------------
    # 5. Keyword Feedback
    # --------------------------------------

    if len(found_keywords) >= 8:
        feedback.append(
            "Good! Your resume contains many relevant job keywords."
        )
    else:
        feedback.append(
            "Add more relevant job-related keywords to improve keyword matching."
        )


    # --------------------------------------
    # 6. Missing Keywords
    # --------------------------------------

    if len(missing_keywords) > 0:
        feedback.append(
            "Consider adding these missing keywords: "
            + ", ".join(missing_keywords[:5])
        )


    # --------------------------------------
    # 7. ATS Feedback
    # --------------------------------------

    if ats_result["score"] >= 80:
        feedback.append(
            "Good! Your resume has good basic ATS compatibility."
        )
    else:
        feedback.append(
            "Improve ATS compatibility by using clear sections such as Skills, Education, Experience, Projects, and Certifications."
        )


    # --------------------------------------
    # 8. Overall Score Feedback
    # --------------------------------------

    if overall_score >= 80:
        feedback.append(
            "Excellent! Your resume has a strong overall score."
        )

    elif overall_score >= 60:
        feedback.append(
            "Good resume, but there is still room for improvement."
        )

    else:
        feedback.append(
            "Your resume needs improvement. Focus on skills, projects, keywords, and ATS compatibility."
        )


    return feedback
# ==========================================
# STEP 16: JOB DESCRIPTION MATCHING
# ==========================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_resume_with_job(resume_text, job_description):
    """
    Compare resume text with a job description.

    Parameters:
        resume_text: Text extracted from the resume
        job_description: Job description text

    Returns:
        float: Match percentage
    """

    # Convert both texts to lowercase
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    # Convert texts into TF-IDF vectors
    vectors = vectorizer.fit_transform(
        [resume_text, job_description]
    )

    # Calculate cosine similarity
    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    # Convert similarity into percentage
    match_percentage = similarity * 100

    return round(match_percentage, 2)
# ==========================================
# STEP 16: JOB DESCRIPTION MATCHING
# ==========================================

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_resume_with_job(resume_text, job_description):
    """
    Compare resume text with a job description.

    Parameters:
        resume_text: Text extracted from the resume
        job_description: Job description text

    Returns:
        float: Match percentage
    """

    # Convert both texts to lowercase
    resume_text = resume_text.lower()
    job_description = job_description.lower()

    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    # Convert texts into TF-IDF vectors
    vectors = vectorizer.fit_transform(
        [resume_text, job_description]
    )

    # Calculate cosine similarity
    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    # Convert similarity into percentage
    match_percentage = similarity * 100

    return round(match_percentage, 2)
# ==========================================
# STEP 17: RESUME ANALYSIS VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt


def create_resume_score_chart(score_result):
    """
    Create a bar chart showing resume score details.

    Parameters:
        score_result: Dictionary returned by
                      calculate_resume_score()

    Returns:
        None
    """

    categories = [
        "Skills",
        "Experience",
        "Education",
        "Projects",
        "Keywords",
        "ATS",
        "Completeness"
    ]

    scores = [
        score_result["skills_score"],
        score_result["experience_score"],
        score_result["education_score"],
        score_result["project_score"],
        score_result["keyword_score"],
        score_result["ats_score"],
        score_result["completeness_score"]
    ]

    plt.figure(figsize=(10, 6))

    plt.bar(categories, scores)

    plt.title("AI Resume Reviewer - Score Analysis")
    plt.xlabel("Resume Categories")
    plt.ylabel("Score")

    plt.ylim(0, 25)

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()