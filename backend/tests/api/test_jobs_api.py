from unittest.mock import Mock

from app.auth.dependencies import get_current_user
from app.constants.job import JobStatus
from app.providers.services import get_job_service


class FakeUser:
    id = 1


def create_job():
    return {
        "id": 1,
        "title": "Backend Developer",
        "company": "OpenAI",
        "location": "Remote",
        "salary": "$5000",
        "description": "Python FastAPI",
        "url": "https://job.test",
        "source": "LinkedIn",
        "status": JobStatus.SAVED,
        "score": 95,
        "user_id": 1,
    }


def test_create_job(client):

    service = Mock()

    service.create_job.return_value = create_job()

    client.app.dependency_overrides[get_job_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.post(
        "/api/jobs",
        json={
            "title": "Backend Developer",
            "company": "OpenAI",
            "location": "Remote",
            "salary": "$5000",
            "description": "Python FastAPI",
            "url": "https://job.test",
            "source": "LinkedIn",
        },
    )

    assert response.status_code == 200

    client.app.dependency_overrides.clear()


def test_get_jobs(client):

    service = Mock()

    service.search_jobs.return_value = []

    client.app.dependency_overrides[get_job_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.get("/api/jobs")

    assert response.status_code == 200

    assert response.json() == []

    client.app.dependency_overrides.clear()


def test_get_job(client):

    service = Mock()

    service.get_job.return_value = create_job()

    client.app.dependency_overrides[get_job_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.get("/api/jobs/1")

    assert response.status_code == 200

    assert response.json()["id"] == 1

    client.app.dependency_overrides.clear()


def test_update_job(client):

    service = Mock()

    updated = create_job()
    updated["title"] = "Senior Backend Developer"

    service.update_job.return_value = updated

    client.app.dependency_overrides[get_job_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.put(
        "/api/jobs/1",
        json={"title": "Senior Backend Developer"},
    )

    assert response.status_code == 200

    assert response.json()["title"] == "Senior Backend Developer"

    client.app.dependency_overrides.clear()


def test_delete_job(client):

    service = Mock()

    service.delete_job.return_value = True

    client.app.dependency_overrides[get_job_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.delete("/api/jobs/1")

    assert response.status_code == 200

    assert response.json() == {"message": "Job deleted successfully."}

    client.app.dependency_overrides.clear()
