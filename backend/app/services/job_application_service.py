from fastapi import HTTPException

from app.models.job_application import JobApplication
from app.repositories.job_application_repository import \
    JobApplicationRepository


class JobApplicationService:

    def __init__(
        self,
        repo: JobApplicationRepository,
    ):
        self.repo = repo

    def create_application(
        self,
        user_id: int,
        job_id: int,
    ):

        existing = self.repo.get_by_user_and_job(
            user_id,
            job_id,
        )

        if existing:
            raise HTTPException(
                status_code=409,
                detail="You have already saved this job.",
            )

        application = JobApplication(
            user_id=user_id,
            job_id=job_id,
            status="Saved",
        )

        return self.repo.create(application)

    def get_user_applications(
        self,
        user_id: int,
    ):
        return self.repo.get_by_user(user_id)

    def update_application(
        self,
        user_id: int,
        application_id: int,
        data,
    ):

        application = self.repo.get_by_id_and_user(
            application_id,
            user_id,
        )

        if application is None:
            return None

        for field, value in data.model_dump(
            exclude_unset=True,
        ).items():
            setattr(
                application,
                field,
                value,
            )

        return self.repo.update(application)

    def delete_application(
        self,
        user_id: int,
        application_id: int,
    ):

        application = self.repo.get_by_id_and_user(
            application_id,
            user_id,
        )

        if application is None:
            return False

        self.repo.delete(application)

        return True
