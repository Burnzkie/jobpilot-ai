from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    company: str
    location: str | None = None
    salary: str | None = None
    description: str | None = None
    url: str
    source: str


class JobUpdate(BaseModel):
    title: str | None = None
    company: str | None = None
    location: str | None = None
    salary: str | None = None
    description: str | None = None
    status: str | None = None
    score: int | None = None


class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str | None
    salary: str | None
    description: str | None
    url: str
    source: str
    status: str
    score: int

    model_config = {"from_attributes": True}
