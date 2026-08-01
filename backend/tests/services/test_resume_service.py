from unittest.mock import Mock, patch

import pytest
from fastapi import UploadFile

from app.models.resume import Resume
from app.services.resume_service import ResumeService


def create_service():

    repo = Mock()
    repo.db = Mock()

    service = ResumeService(repo)

    return service, repo


def create_resume():

    return Resume(
        id=1,
        filename="resume.pdf",
        original_filename="resume.pdf",
        file_path="uploads/resumes/resume.pdf",
        extracted_text="Python FastAPI",
        user_id=1,
    )


def create_upload():

    file = Mock(spec=UploadFile)

    file.filename = "resume.pdf"
    file.file = Mock()

    return file


@patch("app.services.resume_service.extract_text")
@patch("app.services.resume_service.validate_file_size")
@patch("app.services.resume_service.validate_resume")
@patch.object(ResumeService, "_save_uploaded_file")
def test_upload_resume(
    mock_save,
    mock_validate_resume,
    mock_validate_size,
    mock_extract,
):

    service, repo = create_service()

    repo.create.return_value = create_resume()
    repo.update.return_value = create_resume()

    mock_extract.return_value = "Python FastAPI"

    resume = service.upload_resume(
        create_upload(),
        1,
    )

    assert resume.filename == "resume.pdf"

    repo.create.assert_called_once()
    repo.update.assert_called_once()


@patch("app.services.resume_service.validate_file_size")
@patch("app.services.resume_service.validate_resume")
def test_upload_resume_create_failed(
    mock_validate_resume,
    mock_validate_size,
):

    service, repo = create_service()

    repo.create.side_effect = Exception("Database error")

    with pytest.raises(Exception):
        service.upload_resume(
            create_upload(),
            1,
        )


def test_get_user_resumes():

    service, repo = create_service()

    resumes = [create_resume()]

    repo.get_by_user.return_value = resumes

    result = service.get_user_resumes(1)

    assert result == resumes

    repo.get_by_user.assert_called_once_with(1)


def test_get_user_resumes_empty():

    service, repo = create_service()

    repo.get_by_user.return_value = []

    result = service.get_user_resumes(1)

    assert result == []


def test_get_latest_resume():

    service, repo = create_service()

    resume = create_resume()

    repo.get_latest_by_user.return_value = resume

    result = service.get_latest_resume(1)

    assert result == resume

    repo.get_latest_by_user.assert_called_once_with(1)


def test_get_latest_resume_not_found():

    service, repo = create_service()

    repo.get_latest_by_user.return_value = None

    result = service.get_latest_resume(1)

    assert result is None
