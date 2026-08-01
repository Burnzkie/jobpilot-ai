import pytest

from app.models.user import User
from app.repositories.user_repository import UserRepository


@pytest.fixture
def user(db):

    repo = UserRepository(db)

    return repo.create(
        User(
            name="Jude",
            email="jude@example.com",
            password="123456",
        )
    )
