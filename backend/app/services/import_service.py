import logging

from app.repositories.job_repository import JobRepository
from app.schemas.job import JobCreate
from app.scrapers.manager import ScraperManager
from app.services.job_service import JobService

logger = logging.getLogger(__name__)


class ImportService:

    def __init__(
        self,
        repo: JobRepository,
        job_service: JobService,
        manager: ScraperManager,
    ):
        self.repo = repo
        self.job_service = job_service
        self.manager = manager

    def import_jobs(
        self,
        user_id: int,
    ):

        jobs = self.manager.fetch_all()

        imported = 0
        skipped = 0
        errors = 0

        for item in jobs:

            exists = self.repo.get_by_user_and_url(
                user_id=user_id,
                url=item["url"],
            )

            if exists:
                skipped += 1
                continue

            try:

                job = JobCreate(
                    title=item.get("title", ""),
                    company=item.get("company", ""),
                    location=item.get("location"),
                    salary=item.get("salary"),
                    description=item.get("description"),
                    url=item.get("url", ""),
                    source=item.get("source", "unknown"),
                )

                self.job_service.create_job(
                    data=job,
                    user_id=user_id,
                )

                imported += 1

            except Exception:

                logger.exception(
                    "Error importing job '%s'",
                    item.get("title", "Unknown"),
                )

                errors += 1

        logger.info(
            "Import completed. Imported=%s Skipped=%s Errors=%s",
            imported,
            skipped,
            errors,
        )

        return {
            "total": len(jobs),
            "imported": imported,
            "skipped": skipped,
            "errors": errors,
        }
