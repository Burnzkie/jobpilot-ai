from app.models.job import Job
from app.models.user import User
from app.repositories.job_repository import JobRepository
from app.repositories.user_repository import UserRepository


def create_user(db):
    repo = UserRepository(db)

    return repo.create(
        User(
            name="Jude",
            email="jude@example.com",
            password="123456",
        )
    )


def create_job(db, user):
    repo = JobRepository(db)

    return repo.create(
        Job(
            title="Backend Developer",
            company="OpenAI",
            location="Remote",
            salary="$5000",
            description="Python FastAPI",
            url="https://example.com/job1",
            source="LinkedIn",
            status="Saved",
            score=85,
            user_id=user.id,
        )
    )


def test_create_job(db):
    user = create_user(db)

    job = create_job(db, user)

    assert job.id is not None
    assert job.title == "Backend Developer"


def test_get_by_user(db):
    user = create_user(db)

    create_job(db, user)

    repo = JobRepository(db)

    jobs = repo.get_by_user(user.id)

    assert len(jobs) == 1


def test_get_by_user_and_id(db):
    user = create_user(db)

    job = create_job(db, user)

    repo = JobRepository(db)

    found = repo.get_by_user_and_id(
        user.id,
        job.id,
    )

    assert found is not None
    assert found.id == job.id


def test_get_by_user_and_url(db):
    user = create_user(db)

    create_job(db, user)

    repo = JobRepository(db)

    found = repo.get_by_user_and_url(
        user.id,
        "https://example.com/job1",
    )

    assert found is not None


def test_delete_job(db):
    user = create_user(db)

    job = create_job(db, user)

    repo = JobRepository(db)

    repo.delete(job)

    assert repo.get_by_id(job.id) is None
