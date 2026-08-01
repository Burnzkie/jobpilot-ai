import logging
import os
import shutil
import uuid

from fastapi import UploadFile

from app.core.config import settings
from app.database.transaction import transaction
from app.models.resume import Resume
from app.repositories.resume_repository import ResumeRepository
from app.utils.file_validator import validate_file_size, validate_resume
from app.utils.text_extractor import extract_text

logger = logging.getLogger(__name__)

UPLOAD_DIR = settings.RESUME_UPLOAD_DIR


class ResumeService:

    def __init__(
        self,
        repo: ResumeRepository,
    ):
        self.repo = repo

        os.makedirs(UPLOAD_DIR, exist_ok=True)

    def _save_uploaded_file(
        self,
        file: UploadFile,
        path: str,
    ):
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

    def upload_resume(self, file: UploadFile, user_id: int):
        validate_resume(file)
        validate_file_size(file)

        extension = os.path.splitext(file.filename)[1].lower()
        filename = f"{uuid.uuid4()}{extension}"

        path = os.path.join(UPLOAD_DIR, filename)

        # Save uploaded file
        self._save_uploaded_file(
            file,
            path,
        )

        # Create database record
        resume = Resume(
            filename=filename,
            original_filename=file.filename,
            file_path=path,
            extracted_text="",
            user_id=user_id,
        )

        try:

            with transaction(self.repo.db):

                resume = self.repo.create(resume)

                text = extract_text(path)

                logger.debug("Resume text extracted successfully.")

                resume.extracted_text = text

                self.repo.update(resume)

            logger.info("Resume uploaded successfully.")

            return resume

        except Exception:

            logger.exception("Resume upload failed.")

            if os.path.exists(path):
                os.remove(path)

            raise

    def get_user_resumes(self, user_id: int):
        return self.repo.get_by_user(user_id)

    def get_latest_resume(self, user_id: int):
        return self.repo.get_latest_by_user(user_id)
