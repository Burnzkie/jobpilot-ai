from app.constants.job import DEFAULT_JOB_SCORE, JobStatus
from app.core.exceptions import DuplicateResourceException, NotFoundException
from app.database.transaction import transaction
from app.models.job import Job
from app.repositories.job_repository import JobRepository
from app.services.matching_service import MatchingService


class JobService:

    def __init__(
        self,
        repo: JobRepository,
        matcher: MatchingService,
    ):
        self.repo = repo
        self.matcher = matcher

    def _get_user_job(
        self,
        user_id: int,
        job_id: int,
    ) -> Job:
        """
        Returns a job only if it belongs to the user.
        Raises NotFoundException otherwise.
        """
        job = self.repo.get_by_user_and_id(
            user_id,
            job_id,
        )

        if job is None:
            raise NotFoundException("Job not found.")

        return job

    def create_job(
        self,
        data,
        user_id: int,
    ):

        existing = self.repo.get_by_user_and_url(
            user_id,
            data.url,
        )

        if existing:
            raise DuplicateResourceException("This job has already been saved.")

        job = Job(
            title=data.title,
            company=data.company,
            location=data.location,
            salary=data.salary,
            description=data.description,
            url=data.url,
            source=data.source,
            status=JobStatus.SAVED,
            score=DEFAULT_JOB_SCORE,
            user_id=user_id,
        )

        with transaction(self.repo.db):

            job.score = self.matcher.score_job(
                user_id=user_id,
                job=job,
            )

            self.repo.create(job)

        return job

    def get_jobs(
        self,
        user_id: int,
    ):
        return self.repo.get_by_user(user_id)

    def get_job(
        self,
        user_id: int,
        job_id: int,
    ):
        return self._get_user_job(
            user_id,
            job_id,
        )

    def update_job(
        self,
        user_id: int,
        job_id: int,
        data,
    ):

        job = self._get_user_job(
            user_id,
            job_id,
        )

        allowed_fields = {
            "title",
            "company",
            "location",
            "salary",
            "description",
            "url",
            "source",
            "status",
        }

        for field, value in data.model_dump(exclude_unset=True).items():

            if field in allowed_fields:
                setattr(
                    job,
                    field,
                    value,
                )

        with transaction(self.repo.db):
            self.repo.update(job)

        return job

    def delete_job(
        self,
        user_id: int,
        job_id: int,
    ):

        job = self._get_user_job(
            user_id,
            job_id,
        )

        with transaction(self.repo.db):
            self.repo.delete(job)

        return True

    def change_status(
        self,
        user_id: int,
        job_id: int,
        status: str,
    ):

        job = self._get_user_job(
            user_id,
            job_id,
        )

        job.status = status

        with transaction(self.repo.db):
            self.repo.update(job)

        return job

    def search_jobs(
        self,
        user_id: int,
        page: int,
        limit: int,
        search: str | None,
        status: str | None,
        company: str | None,
    ):

        return self.repo.search_jobs(
            user_id=user_id,
            page=page,
            limit=limit,
            search=search,
            status=status,
            company=company,
        )
