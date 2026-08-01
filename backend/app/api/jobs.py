from fastapi import APIRouter, Depends, Query

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.providers.services import get_import_service, get_job_service
from app.schemas.job import JobCreate, JobResponse, JobUpdate
from app.services.import_service import ImportService
from app.services.job_service import JobService

router = APIRouter(
    prefix="/api/jobs",
    tags=["Jobs"],
)


@router.post("", response_model=JobResponse)
def create_job(
    data: JobCreate,
    service: JobService = Depends(get_job_service),
    current_user: User = Depends(get_current_user),
):
    return service.create_job(
        data=data,
        user_id=current_user.id,
    )


@router.post("/import")
def import_jobs(
    service: ImportService = Depends(get_import_service),
    current_user: User = Depends(get_current_user),
):
    return service.import_jobs(user_id=current_user.id)


@router.get("", response_model=list[JobResponse])
def get_jobs(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    search: str | None = None,
    status: str | None = None,
    company: str | None = None,
    service: JobService = Depends(get_job_service),
    current_user: User = Depends(get_current_user),
):
    return service.search_jobs(
        user_id=current_user.id,
        page=page,
        limit=limit,
        search=search,
        status=status,
        company=company,
    )


@router.get("/{job_id}", response_model=JobResponse)
def get_job(
    job_id: int,
    service: JobService = Depends(get_job_service),
    current_user: User = Depends(get_current_user),
):
    return service.get_job(
        user_id=current_user.id,
        job_id=job_id,
    )


@router.put("/{job_id}", response_model=JobResponse)
def update_job(
    job_id: int,
    data: JobUpdate,
    service: JobService = Depends(get_job_service),
    current_user: User = Depends(get_current_user),
):
    return service.update_job(
        user_id=current_user.id,
        job_id=job_id,
        data=data,
    )


@router.delete("/{job_id}")
def delete_job(
    job_id: int,
    service: JobService = Depends(get_job_service),
    current_user: User = Depends(get_current_user),
):
    service.delete_job(
        user_id=current_user.id,
        job_id=job_id,
    )

    return {"message": "Job deleted successfully."}
