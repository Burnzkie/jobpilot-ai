from typing import TypeVar

from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, model: T) -> T:
        self.add(model)
        self.flush()
        self.refresh(model)
        return model

    def add(self, model: T) -> None:
        self.db.add(model)

    def delete(self, model: T) -> None:
        self.db.delete(model)
        self.flush()

    def flush(self) -> None:
        self.db.flush()

    def refresh(self, model: T) -> None:
        self.db.refresh(model)

    def merge(self, model: T) -> T:
        return self.db.merge(model)

    def expunge(self, model: T) -> None:
        self.db.expunge(model)
