from app.models.job import Job
from app.repositories.base_repository import BaseRepository


class JobRepository(BaseRepository):

    def __init__(self, db):
        super().__init__(db)

    def get_by_id(self, job_id: int):
        return self.db.query(Job).filter(Job.id == job_id).first()

    def get_by_user(self, user_id: int):
        return (
            self.db.query(Job)
            .filter(Job.user_id == user_id)
            .order_by(Job.created_at.desc())
            .all()
        )

    def get_by_user_and_id(
        self,
        user_id: int,
        job_id: int,
    ):
        return (
            self.db.query(Job)
            .filter(
                Job.user_id == user_id,
                Job.id == job_id,
            )
            .first()
        )

    def get_by_user_and_url(
        self,
        user_id: int,
        url: str,
    ):
        return (
            self.db.query(Job)
            .filter(
                Job.user_id == user_id,
                Job.url == url,
            )
            .first()
        )

    def search_jobs(
        self,
        user_id: int,
        page: int,
        limit: int,
        search: str | None = None,
        status: str | None = None,
        company: str | None = None,
    ):
        query = self.db.query(Job).filter(Job.user_id == user_id)

        if search:
            query = query.filter(Job.title.ilike(f"%{search}%"))

        if status:
            query = query.filter(Job.status == status)

        if company:
            query = query.filter(Job.company.ilike(f"%{company}%"))

        return (
            query.order_by(Job.created_at.desc())
            .offset((page - 1) * limit)
            .limit(limit)
            .all()
        )

    def update(self, job: Job):
        self.flush()
        self.refresh(job)
        return job

    def delete(self, job: Job):
        super().delete(job)
        self.flush()
