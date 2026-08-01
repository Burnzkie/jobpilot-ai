import logging

from app.auth.hashing import hash_password, verify_password
from app.auth.jwt_handler import create_access_token
from app.core.exceptions import DuplicateResourceException
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserLogin, UserRegister

logger = logging.getLogger(__name__)


class AuthService:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, data: UserRegister):

        existing = self.repo.get_by_email(data.email)

        if existing:

            raise DuplicateResourceException("Email already exists.")

        user = User(
            name=data.name, email=data.email, password=hash_password(data.password)
        )

        return self.repo.create(user)

    def login(self, data: UserLogin):

        user = self.repo.get_by_email(data.email)

        if not user:

            return None

        if not verify_password(data.password, user.password):

            return None

        token = create_access_token({"sub": str(user.id)})

        return token
