from fastapi import APIRouter, Depends, HTTPException

# Adjust these imports if your project uses different paths
from app.auth.dependencies import get_current_user
from app.models.user import User
from app.providers.services import get_job_application_service
from app.schemas.job_application import (JobApplicationCreate,
                                         JobApplicationResponse,
                                         JobApplicationUpdate)
from app.services.job_application_service import JobApplicationService

router = APIRouter(prefix="/api/applications", tags=["Applications"])


@router.post("", response_model=JobApplicationResponse)
def create_application(
    data: JobApplicationCreate,
    service: JobApplicationService = Depends(get_job_application_service),
    current_user: User = Depends(get_current_user),
):

    return service.create_application(user_id=current_user.id, job_id=data.job_id)


@router.get("", response_model=list[JobApplicationResponse])
def get_applications(
    service: JobApplicationService = Depends(get_job_application_service),
    current_user: User = Depends(get_current_user),
):

    return service.get_user_applications(current_user.id)


@router.put("/{application_id}", response_model=JobApplicationResponse)
def update_application(
    application_id: int,
    data: JobApplicationUpdate,
    service: JobApplicationService = Depends(get_job_application_service),
    current_user: User = Depends(get_current_user),
):

    application = service.update_application(
        user_id=current_user.id, application_id=application_id, data=data
    )

    if application is None:
        raise HTTPException(status_code=404, detail="Application not found.")

    return application


@router.delete("/{application_id}")
def delete_application(
    application_id: int,
    service: JobApplicationService = Depends(get_job_application_service),
    current_user: User = Depends(get_current_user),
):

    deleted = service.delete_application(
        user_id=current_user.id, application_id=application_id
    )

    if not deleted:
        raise HTTPException(status_code=404, detail="Application not found.")

    return {"message": "Application deleted successfully."}
