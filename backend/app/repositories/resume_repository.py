from app.models.resume import Resume
from app.repositories.base_repository import BaseRepository


class ResumeRepository(BaseRepository):

    def __init__(self, db):
        super().__init__(db)

    def get_by_user(self, user_id: int):
        return (
            self.db.query(Resume)
            .filter(Resume.user_id == user_id)
            .order_by(Resume.created_at.desc())
            .all()
        )

    def get_by_id(self, resume_id: int):
        return self.db.query(Resume).filter(Resume.id == resume_id).first()

    def get_latest_by_user(self, user_id: int):
        return (
            self.db.query(Resume)
            .filter(Resume.user_id == user_id)
            .order_by(Resume.created_at.desc())
            .first()
        )

    def update(self, resume: Resume):
        self.flush()
        self.refresh(resume)
        return resume

    def delete(self, resume: Resume):
        super().delete(resume)
