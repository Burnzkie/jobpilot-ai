from unittest.mock import Mock

from app.providers.services import get_cover_letter_service


def test_generate_cover_letter(client):

    service = Mock()

    service.create.return_value = (
        "Dear Hiring Manager,\n\n"
        "I am excited to apply for the Backend Developer position."
    )

    client.app.dependency_overrides[get_cover_letter_service] = lambda: service

    response = client.post(
        "/api/cover-letter",
        json={
            "name": "Jude",
            "job_title": "Backend Developer",
            "company": "OpenAI",
            "resume_skills": ["Python", "FastAPI", "MySQL"],
            "job_description": (
                "Looking for a Python developer " "with FastAPI experience."
            ),
        },
    )

    assert response.status_code == 200

    assert "Dear Hiring Manager" in response.json()["cover_letter"]

    service.create.assert_called_once()

    client.app.dependency_overrides.clear()
