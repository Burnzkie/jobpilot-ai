from app.ai.embedding import similarity


def calculate_match_score(resume_text: str, job_text: str):
    """
    Returns a score from 0 to 100.
    """

    score = similarity(resume_text, job_text)

    return round(score * 100, 2)
