import pytest

from app.models.job import Job
from app.repositories.job_repository import JobRepository


@pytest.fixture
def job(db, user):

    repo = JobRepository(db)

    return repo.create(
        Job(
            title="Backend Developer",
            company="OpenAI",
            location="Remote",
            salary="$5000",
            description="Python FastAPI",
            url="https://example.com/job",
            source="LinkedIn",
            status="Saved",
            score=85,
            user_id=user.id,
        )
    )
