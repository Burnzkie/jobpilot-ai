from pathlib import Path

from fastapi import UploadFile

from app.core.config import settings
from app.core.exceptions import ValidationException

ALLOWED_EXTENSIONS = set(settings.ALLOWED_UPLOAD_EXTENSIONS)

ALLOWED_CONTENT_TYPES = set(settings.ALLOWED_CONTENT_TYPES)

MAX_FILE_SIZE = settings.MAX_UPLOAD_SIZE


def validate_resume(file: UploadFile):

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:

        raise ValidationException("Only PDF and DOCX files are allowed.")

    if file.content_type not in ALLOWED_CONTENT_TYPES:

        raise ValidationException("Invalid file type.")


def validate_file_size(file: UploadFile):

    file.file.seek(0, 2)

    size = file.file.tell()

    file.file.seek(0)

    if size > MAX_FILE_SIZE:

        raise ValidationException("Maximum file size is 5 MB.")
