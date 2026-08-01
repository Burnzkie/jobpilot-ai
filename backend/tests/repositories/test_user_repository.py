from app.models.user import User
from app.repositories.user_repository import UserRepository


def test_create_user(db):
    repo = UserRepository(db)

    user = User(
        name="Jude",
        email="jude@example.com",
        password="hashed-password",
    )

    created = repo.create(user)

    assert created.id is not None
    assert created.email == "jude@example.com"
    assert created.name == "Jude"


def test_get_by_email(db):
    repo = UserRepository(db)

    user = User(
        name="John",
        email="john@example.com",
        password="123456",
    )

    repo.create(user)

    found = repo.get_by_email("john@example.com")

    assert found is not None
    assert found.email == "john@example.com"


def test_get_by_email_not_found(db):
    repo = UserRepository(db)

    found = repo.get_by_email("missing@example.com")

    assert found is None


def test_get_by_id(db):
    repo = UserRepository(db)

    user = User(
        name="Jane",
        email="jane@example.com",
        password="123456",
    )

    created = repo.create(user)

    found = repo.get_by_id(created.id)

    assert found is not None
    assert found.id == created.id


def test_get_by_id_not_found(db):
    repo = UserRepository(db)

    found = repo.get_by_id(99999)

    assert found is None
