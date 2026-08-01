from unittest.mock import Mock

import pytest

from app.auth.hashing import hash_password
from app.core.exceptions import DuplicateResourceException
from app.schemas.user import UserLogin, UserRegister
from app.services.auth_service import AuthService


def test_register_creates_user():

    repo = Mock()

    repo.get_by_email.return_value = None

    repo.create.return_value = Mock(id=1, name="Jude", email="jude@test.com")

    service = AuthService(repo)

    data = UserRegister(name="Jude", email="jude@test.com", password="password123")

    user = service.register(data)

    assert user.email == "jude@test.com"

    repo.create.assert_called_once()


def test_register_duplicate_email():

    repo = Mock()

    # Simulate an existing user with the same email
    repo.get_by_email.return_value = Mock()

    service = AuthService(repo)

    data = UserRegister(name="Jude", email="jude@test.com", password="password123")

    with pytest.raises(DuplicateResourceException):
        service.register(data)

    # Ensure no new user is created
    repo.create.assert_not_called()


def test_login_success():

    repo = Mock()

    user = Mock()
    user.id = 1
    user.password = hash_password("password123")

    repo.get_by_email.return_value = user

    service = AuthService(repo)

    token = service.login(UserLogin(email="jude@test.com", password="password123"))

    assert token is not None
    assert isinstance(token, str)


def test_login_wrong_password():

    repo = Mock()

    user = Mock()
    user.id = 1
    user.password = hash_password("password123")

    repo.get_by_email.return_value = user

    service = AuthService(repo)

    token = service.login(UserLogin(email="jude@test.com", password="wrongpassword"))

    assert token is None
