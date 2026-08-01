from app.models.job_application import JobApplication
from app.repositories.base_repository import BaseRepository


class JobApplicationRepository(BaseRepository):

    def __init__(self, db):
        super().__init__(db)

    def get_by_id(self, application_id: int):
        return (
            self.db.query(JobApplication)
            .filter(JobApplication.id == application_id)
            .first()
        )

    def get_by_id_and_user(self, application_id: int, user_id: int):
        return (
            self.db.query(JobApplication)
            .filter(
                JobApplication.id == application_id, JobApplication.user_id == user_id
            )
            .first()
        )

    def get_by_user(self, user_id: int):
        return (
            self.db.query(JobApplication)
            .filter(JobApplication.user_id == user_id)
            .order_by(JobApplication.created_at.desc())
            .all()
        )

    def get_by_user_and_job(self, user_id: int, job_id: int):
        return (
            self.db.query(JobApplication)
            .filter(JobApplication.user_id == user_id, JobApplication.job_id == job_id)
            .first()
        )

    def update(self, application: JobApplication):
        self.flush()
        self.refresh(application)
        return application

    def delete(self, application: JobApplication):
        super().delete(application)
