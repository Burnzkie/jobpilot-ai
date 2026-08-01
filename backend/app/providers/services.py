from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.repositories.job_application_repository import \
    JobApplicationRepository
from app.repositories.job_repository import JobRepository
from app.repositories.resume_repository import ResumeRepository
from app.repositories.user_repository import UserRepository
from app.scrapers.manager import ScraperManager
from app.services.auth_service import AuthService
from app.services.cover_letter_service import CoverLetterService
from app.services.import_service import ImportService
from app.services.job_application_service import JobApplicationService
from app.services.job_service import JobService
from app.services.matching_service import MatchingService
from app.services.resume_service import ResumeService

# ==========================
# Repositories
# ==========================


def get_user_repository(
    db: Session = Depends(get_db),
) -> UserRepository:
    return UserRepository(db)


def get_job_repository(
    db: Session = Depends(get_db),
) -> JobRepository:
    return JobRepository(db)


def get_resume_repository(
    db: Session = Depends(get_db),
) -> ResumeRepository:
    return ResumeRepository(db)


def get_job_application_repository(
    db: Session = Depends(get_db),
) -> JobApplicationRepository:
    return JobApplicationRepository(db)


# ==========================
# Services
# ==========================


def get_matching_service(
    repo: ResumeRepository = Depends(get_resume_repository),
) -> MatchingService:
    return MatchingService(repo)


def get_auth_service(
    repo: UserRepository = Depends(get_user_repository),
) -> AuthService:
    return AuthService(repo)


def get_resume_service(
    repo: ResumeRepository = Depends(get_resume_repository),
) -> ResumeService:
    return ResumeService(repo)


def get_job_service(
    repo: JobRepository = Depends(get_job_repository),
    matcher: MatchingService = Depends(get_matching_service),
) -> JobService:
    return JobService(
        repo=repo,
        matcher=matcher,
    )


def get_scraper_manager() -> ScraperManager:
    return ScraperManager()


def get_import_service(
    repo: JobRepository = Depends(get_job_repository),
    job_service: JobService = Depends(get_job_service),
    manager: ScraperManager = Depends(get_scraper_manager),
) -> ImportService:
    return ImportService(
        repo=repo,
        job_service=job_service,
        manager=manager,
    )


def get_cover_letter_service() -> CoverLetterService:
    return CoverLetterService()


def get_job_application_service(
    repo: JobApplicationRepository = Depends(get_job_application_repository),
) -> JobApplicationService:
    return JobApplicationService(repo)
