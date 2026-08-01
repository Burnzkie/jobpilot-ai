from unittest.mock import Mock

from app.auth.dependencies import get_current_user
from app.providers.services import get_job_application_service


class FakeUser:
    id = 1


def create_application():
    return {
        "id": 1,
        "user_id": 1,
        "job_id": 1,
        "status": "Saved",
        "notes": None,
        "applied_date": None,
    }


def test_create_application(client):

    service = Mock()

    service.create_application.return_value = create_application()

    client.app.dependency_overrides[get_job_application_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.post(
        "/api/applications",
        json={"job_id": 1},
    )

    assert response.status_code == 200

    assert response.json()["job_id"] == 1

    client.app.dependency_overrides.clear()


def test_get_applications(client):

    service = Mock()

    service.get_user_applications.return_value = [create_application()]

    client.app.dependency_overrides[get_job_application_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.get("/api/applications")

    assert response.status_code == 200

    assert len(response.json()) == 1

    client.app.dependency_overrides.clear()


def test_update_application(client):

    service = Mock()

    application = create_application()
    application["status"] = "Applied"

    service.update_application.return_value = application

    client.app.dependency_overrides[get_job_application_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.put(
        "/api/applications/1",
        json={"status": "Applied"},
    )

    assert response.status_code == 200

    assert response.json()["status"] == "Applied"

    client.app.dependency_overrides.clear()


def test_update_application_not_found(client):

    service = Mock()

    service.update_application.return_value = None

    client.app.dependency_overrides[get_job_application_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.put(
        "/api/applications/999",
        json={"status": "Applied"},
    )

    assert response.status_code == 404

    client.app.dependency_overrides.clear()


def test_delete_application(client):

    service = Mock()

    service.delete_application.return_value = True

    client.app.dependency_overrides[get_job_application_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.delete("/api/applications/1")

    assert response.status_code == 200

    assert response.json() == {"message": "Application deleted successfully."}

    client.app.dependency_overrides.clear()


def test_delete_application_not_found(client):

    service = Mock()

    service.delete_application.return_value = False

    client.app.dependency_overrides[get_job_application_service] = lambda: service

    client.app.dependency_overrides[get_current_user] = lambda: FakeUser()

    response = client.delete("/api/applications/999")

    assert response.status_code == 404

    client.app.dependency_overrides.clear()
