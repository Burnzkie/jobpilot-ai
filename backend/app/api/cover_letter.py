from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.providers.services import get_cover_letter_service
from app.services.cover_letter_service import CoverLetterService

router = APIRouter(prefix="/api/cover-letter", tags=["Cover Letter"])


class CoverLetterRequest(BaseModel):

    name: str

    job_title: str

    company: str

    resume_skills: list[str]

    job_description: str


@router.post("")
def create_cover_letter(
    data: CoverLetterRequest,
    service: CoverLetterService = Depends(get_cover_letter_service),
):

    letter = service.create(data)

    return {"cover_letter": letter}
