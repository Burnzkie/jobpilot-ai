from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from app.constants.job import DEFAULT_JOB_SCORE, JobStatus
from app.database.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    company = Column(String(255), nullable=False)

    location = Column(String(255), nullable=True)

    salary = Column(String(255), nullable=True)

    description = Column(Text, nullable=True)

    url = Column(String(500), nullable=False)

    source = Column(String(100), nullable=False)

    status = Column(String(50), default=JobStatus.SAVED)

    score = Column(Integer, default=DEFAULT_JOB_SCORE)

    user_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
