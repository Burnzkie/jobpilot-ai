from datetime import datetime

from pydantic import BaseModel


class JobApplicationCreate(BaseModel):

    job_id: int


class JobApplicationUpdate(BaseModel):

    status: str | None = None

    notes: str | None = None


class JobApplicationResponse(BaseModel):

    id: int
    job_id: int
    user_id: int
    status: str

    notes: str | None = None

    applied_date: datetime | None = None

    model_config = {"from_attributes": True}
