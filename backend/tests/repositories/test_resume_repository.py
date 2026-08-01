from app.models.resume import Resume
from app.models.user import User
from app.repositories.resume_repository import ResumeRepository
from app.repositories.user_repository import UserRepository


def create_user(db):
    return UserRepository(db).create(
        User(
            name="Jude",
            email="jude@example.com",
            password="123456",
        )
    )


def create_resume(db, user):
    return ResumeRepository(db).create(
        Resume(
            filename="resume.pdf",
            original_filename="resume.pdf",
            file_path="/tmp/resume.pdf",
            extracted_text="Python FastAPI SQL",
            user_id=user.id,
        )
    )


def test_get_by_user(db):
    user = create_user(db)

    create_resume(db, user)

    repo = ResumeRepository(db)

    resumes = repo.get_by_user(user.id)

    assert len(resumes) == 1


def test_get_latest_by_user(db):
    user = create_user(db)

    create_resume(db, user)

    repo = ResumeRepository(db)

    latest = repo.get_latest_by_user(user.id)

    assert latest is not None
    assert latest.filename == "resume.pdf"


def test_get_by_id(db):
    user = create_user(db)

    resume = create_resume(db, user)

    repo = ResumeRepository(db)

    found = repo.get_by_id(resume.id)

    assert found is not None


def test_delete_resume(db):
    user = create_user(db)

    resume = create_resume(db, user)

    repo = ResumeRepository(db)

    repo.delete(resume)

    assert repo.get_by_id(resume.id) is None
