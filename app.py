import streamlit as st

from resume_reviewer import (
    extract_text_from_pdf,
    preprocess_text,
    extract_skills,
    extract_education,
    analyze_experience,
    analyze_projects,
    keyword_analysis,
    ats_check,
    calculate_resume_score,
    generate_feedback,
    match_resume_with_job
)


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Resume Reviewer",
    page_icon="📄",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("📄 AI Resume Reviewer")

st.write(
    "Upload your resume to analyze skills, education, "
    "experience, projects, keywords, ATS compatibility, "
    "resume score, and job matching."
)


# ==========================================
# RESUME UPLOAD
# ==========================================

uploaded_file = st.file_uploader(
    "Upload your Resume PDF",
    type=["pdf"]
)


# ==========================================
# ANALYZE RESUME
# ==========================================

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract text
    resume_text = extract_text_from_pdf(uploaded_file)

    if resume_text.strip() == "":
        st.error(
            "Could not extract text from this PDF. "
            "Please upload a text-based PDF."
        )

    else:

        # Preprocess text
        cleaned_text = preprocess_text(resume_text)

        # ==========================================
        # RESUME ANALYSIS
        # ==========================================

        skills = extract_skills(cleaned_text)

        education = extract_education(cleaned_text)

        experience = analyze_experience(cleaned_text)

        projects = analyze_projects(cleaned_text)

        (
            found_keywords,
            missing_keywords,
            keyword_percentage
        ) = keyword_analysis(cleaned_text)

        ats_result = ats_check(cleaned_text)


        # ==========================================
        # RESUME SCORE
        # ==========================================

        score_result = calculate_resume_score(
            skills,
            experience,
            education,
            projects,
            keyword_percentage,
            ats_result["score"]
        )

        overall_score = score_result["overall_score"]


        # ==========================================
        # FEEDBACK
        # ==========================================

        feedback = generate_feedback(
            skills,
            experience,
            education,
            projects,
            found_keywords,
            missing_keywords,
            ats_result,
            overall_score
        )


        # ==========================================
        # DISPLAY OVERALL SCORE
        # ==========================================

        st.header("📊 Resume Score")

        st.metric(
            "Overall Resume Score",
            f"{overall_score} / 100"
        )


        # ==========================================
        # SCORE BREAKDOWN
        # ==========================================

        st.subheader("Score Breakdown")

        score_data = {
            "Skills": score_result["skills_score"],
            "Experience": score_result["experience_score"],
            "Education": score_result["education_score"],
            "Projects": score_result["project_score"],
            "Keywords": score_result["keyword_score"],
            "ATS": score_result["ats_score"],
            "Completeness": score_result["completeness_score"]
        }

        st.bar_chart(score_data)


        # ==========================================
        # SKILLS
        # ==========================================

        st.header("🛠️ Skills")

        if skills:
            st.write(", ".join(skill.title() for skill in skills))
        else:
            st.warning("No technical skills detected.")


        # ==========================================
        # EDUCATION
        # ==========================================

        st.header("🎓 Education")

        if education:
            st.write(
                ", ".join(item.title() for item in education)
            )
        else:
            st.warning("No education information detected.")


        # ==========================================
        # EXPERIENCE
        # ==========================================

        st.header("💼 Experience")

        if experience:
            st.write(
                ", ".join(item.title() for item in experience)
            )
        else:
            st.warning("No experience information detected.")


        # ==========================================
        # PROJECTS
        # ==========================================

        st.header("🚀 Projects")

        if projects:
            st.write(
                ", ".join(item.title() for item in projects)
            )
        else:
            st.warning("No project information detected.")


        # ==========================================
        # KEYWORD ANALYSIS
        # ==========================================

        st.header("🔑 Keyword Analysis")

        st.metric(
            "Keyword Match",
            f"{keyword_percentage}%"
        )

        st.write("### Found Keywords")

        if found_keywords:
            st.write(
                ", ".join(
                    keyword.title()
                    for keyword in found_keywords
                )
            )
        else:
            st.write("No important keywords found.")


        st.write("### Missing Keywords")

        if missing_keywords:
            st.write(
                ", ".join(
                    keyword.title()
                    for keyword in missing_keywords
                )
            )
        else:
            st.success("No important keywords are missing.")


        # ==========================================
        # ATS COMPATIBILITY
        # ==========================================

        st.header("🤖 ATS Compatibility")

        st.metric(
            "ATS Score",
            f"{ats_result['score']} / 100"
        )

        st.write("### Found Sections")

        if ats_result["found_sections"]:
            st.write(
                ", ".join(
                    section.title()
                    for section in ats_result["found_sections"]
                )
            )

        st.write("### Missing Sections")

        if ats_result["missing_sections"]:
            st.write(
                ", ".join(
                    section.title()
                    for section in ats_result["missing_sections"]
                )
            )


        # ==========================================
        # FEEDBACK
        # ==========================================

        st.header("💡 Resume Feedback")

        for item in feedback:
            st.write("• " + item)


        # ==========================================
        # JOB DESCRIPTION MATCHING
        # ==========================================

        st.header("🎯 Job Description Matching")

        job_description = st.text_area(
            "Paste the Job Description here:"
        )

        if st.button("Check Job Match"):

            if job_description.strip() == "":
                st.warning(
                    "Please enter a job description."
                )

            else:

                job_match = match_resume_with_job(
                    cleaned_text,
                    job_description
                )

                st.success(
                    f"Resume–Job Match: {job_match}%"
                )


        # ==========================================
        # EXTRACTED RESUME TEXT
        # ==========================================

        with st.expander("📄 View Extracted Resume Text"):

            st.write(resume_text)