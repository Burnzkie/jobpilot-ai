from unittest.mock import Mock


def test_register_success(client, monkeypatch):

    service = Mock()

    service.register.return_value = {
        "id": 1,
        "name": "Jude",
        "email": "jude@test.com",
    }

    app = client.app

    from app.providers.services import get_auth_service

    app.dependency_overrides[get_auth_service] = lambda: service

    response = client.post(
        "/api/auth/register",
        json={
            "name": "Jude",
            "email": "jude@test.com",
            "password": "password123",
        },
    )

    assert response.status_code == 200

    app.dependency_overrides.clear()


def test_login_success(client):

    service = Mock()

    service.login.return_value = "jwt-token"

    from app.providers.services import get_auth_service

    client.app.dependency_overrides[get_auth_service] = lambda: service

    response = client.post(
        "/api/auth/login",
        json={
            "email": "jude@test.com",
            "password": "password123",
        },
    )

    assert response.status_code == 200

    assert response.json()["access_token"] == "jwt-token"

    client.app.dependency_overrides.clear()


def test_login_invalid_password(client):

    service = Mock()

    service.login.return_value = None

    from app.providers.services import get_auth_service

    client.app.dependency_overrides[get_auth_service] = lambda: service

    response = client.post(
        "/api/auth/login",
        json={
            "email": "jude@test.com",
            "password": "wrongpassword",
        },
    )

    assert response.status_code == 401

    client.app.dependency_overrides.clear()
