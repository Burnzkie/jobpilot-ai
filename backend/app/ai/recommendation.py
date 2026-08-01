# =====================================================
# backend/app/ai/recommendation.py
# =====================================================

from app.ai.job_parser import parse_job


def analyze_resume_against_job(
    resume_skills: list[str],
    job_description: str,
):
    """
    Compare resume skills with a job description.
    """

    parsed_job = parse_job(job_description)

    job_skills = parsed_job["skills"]

    matching = []

    missing = []

    # ----------------------------------------
    # Compare resume skills with job skills
    # ----------------------------------------
    for skill in job_skills:

        if skill.lower() in [s.lower() for s in resume_skills]:

            matching.append(skill)

        else:

            missing.append(skill)

    # ----------------------------------------
    # Generate recommendation
    # ----------------------------------------
    recommendation = ""

    if len(missing) == 0:

        recommendation = "Excellent match. " "Your resume covers all required skills."

    elif len(missing) <= 2:

        recommendation = (
            "Strong candidate. "
            "Learning the missing skills could improve your chances."
        )

    else:

        recommendation = (
            "Several important skills are missing. "
            "Consider strengthening these areas before applying."
        )

    # ----------------------------------------
    # Return analysis
    # ----------------------------------------
    return {
        "matching_skills": matching,
        "missing_skills": missing,
        "recommendation": recommendation,
        "total_required": len(job_skills),
    }
