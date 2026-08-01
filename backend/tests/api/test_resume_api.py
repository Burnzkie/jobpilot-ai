from unittest.mock import Mock

from app.auth.dependencies import get_current_user
from app.providers.services import get_resume_service


class FakeUser:
    id = 1


def create_resume():
    return {
        "id": 1,
        "filename": "resume.pdf",
        "original_filename": "resume.pdf",
        "file_path": "uploads/resumes/resume.pdf",
        "extracted_text": "Python FastAPI",
        "user_id": 1,
    }


def test_upload_resume(client):

    service = Mock()

    service.upload_resume.return_value = create_resume()

    client.app.dependency_overrides[get_resume_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.post(
        "/api/resumes/upload",
        files={
            "file": (
                "resume.pdf",
                b"dummy resume",
                "application/pdf",
            )
        },
    )

    assert response.status_code == 200

    assert response.json()["filename"] == "resume.pdf"

    client.app.dependency_overrides.clear()


def test_get_resumes(client):

    service = Mock()

    service.get_user_resumes.return_value = [create_resume()]

    client.app.dependency_overrides[get_resume_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.get("/api/resumes")

    assert response.status_code == 200

    assert len(response.json()) == 1

    client.app.dependency_overrides.clear()


def test_get_latest_resume(client):

    service = Mock()

    service.get_latest_resume.return_value = create_resume()

    client.app.dependency_overrides[get_resume_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.get("/api/resumes/latest")

    assert response.status_code == 200

    assert response.json()["filename"] == "resume.pdf"

    client.app.dependency_overrides.clear()
