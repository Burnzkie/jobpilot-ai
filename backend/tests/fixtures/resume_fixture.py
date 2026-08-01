import pytest

from app.models.resume import Resume
from app.repositories.resume_repository import ResumeRepository


@pytest.fixture
def resume(db, user):

    repo = ResumeRepository(db)

    return repo.create(
        Resume(
            filename="resume.pdf",
            original_filename="resume.pdf",
            file_path="/tmp/resume.pdf",
            extracted_text="Python FastAPI SQL",
            user_id=user.id,
        )
    )
