from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.providers.services import get_resume_service
from app.schemas.resume import ResumeResponse
from app.services.resume_service import ResumeService

router = APIRouter(prefix="/api/resumes", tags=["Resume"])


@router.post("/upload", response_model=ResumeResponse)
def upload_resume(
    file: UploadFile = File(...),
    service: ResumeService = Depends(get_resume_service),
    current_user: User = Depends(get_current_user),
):
    return service.upload_resume(file=file, user_id=current_user.id)


@router.get("", response_model=list[ResumeResponse])
def get_resumes(
    service: ResumeService = Depends(get_resume_service),
    current_user: User = Depends(get_current_user),
):
    return service.get_user_resumes(current_user.id)


@router.get("/latest", response_model=ResumeResponse)
def get_latest_resume(
    service: ResumeService = Depends(get_resume_service),
    current_user: User = Depends(get_current_user),
):

    resume = service.get_latest_resume(current_user.id)

    if resume is None:
        raise HTTPException(
            status_code=404,
            detail="No resume found.",
        )

    return resume
