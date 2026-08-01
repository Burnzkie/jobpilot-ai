from app.ai.embedding import similarity
from app.ai.job_parser import parse_job
from app.ai.resume_parser import parse_resume
from app.ai.skill_matcher import skill_match


def calculate_ai_score(resume_text: str, job_text: str):

    # Semantic Similarity
    semantic_score = similarity(resume_text, job_text) * 100

    # Structured Parsing
    resume = parse_resume(resume_text)

    job = parse_job(job_text)

    # Skills Matching
    skill_result = skill_match(resume["skills"], job["skills"])

    skill_score = skill_result["score"]

    # Weighted Score
    overall = semantic_score * 0.40 + skill_score * 0.60

    return {
        "overall": round(overall, 2),
        "semantic": round(semantic_score, 2),
        "skills": skill_score,
        "matched_skills": skill_result["matched"],
        "missing_skills": skill_result["missing"],
    }
