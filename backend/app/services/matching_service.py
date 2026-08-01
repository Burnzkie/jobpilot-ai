from app.ai.scoring import calculate_ai_score
from app.constants.job import DEFAULT_JOB_SCORE
from app.models.job import Job
from app.repositories.resume_repository import ResumeRepository


class MatchingService:

    def __init__(
        self,
        resume_repo: ResumeRepository,
    ):
        self.resume_repo = resume_repo

    def score_job(
        self,
        user_id: int,
        job: Job,
    ) -> int:

        resume = self.resume_repo.get_latest_by_user(user_id)

        if resume is None:
            return DEFAULT_JOB_SCORE

        result = calculate_ai_score(
            resume.extracted_text or "",
            job.description or "",
        )

        return int(result["overall"])
