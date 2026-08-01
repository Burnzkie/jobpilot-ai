# =====================================================
# backend/app/ai/cover_letter.py
# =====================================================

from app.ai.job_parser import parse_job


def generate_cover_letter(
    name: str,
    job_title: str,
    company: str,
    resume_skills: list[str],
    job_description: str,
):

    parsed = parse_job(job_description)

    skills = parsed["skills"]

    matched = []

    for skill in skills:

        if skill.lower() in [s.lower() for s in resume_skills]:

            matched.append(skill)

    skill_text = ", ".join(matched)

    letter = f"""
Dear Hiring Manager,

I am writing to express my interest in the {job_title} position at {company}.

My background includes experience with {skill_text}, and I am passionate about building reliable, scalable software solutions.

I am eager to contribute my technical skills, continue learning, and become a valuable member of your team.

Thank you for considering my application. I look forward to discussing how I can contribute to your organization.

Sincerely,

{name}
"""

    return letter.strip()
