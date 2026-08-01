from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from app.models.job_application import JobApplication
from app.services.job_application_service import JobApplicationService


def create_service():
    repo = Mock()

    service = JobApplicationService.__new__(JobApplicationService)
    service.repo = repo

    return service, repo


def create_application():
    return JobApplication(
        id=1,
        user_id=1,
        job_id=1,
        status="Saved",
    )


def create_update_request():
    data = Mock()

    data.model_dump.return_value = {"status": "Applied"}

    return data


def test_create_application():

    service, repo = create_service()

    repo.get_by_user_and_job.return_value = None
    repo.create.return_value = create_application()

    application = service.create_application(
        user_id=1,
        job_id=1,
    )

    assert application.job_id == 1

    repo.create.assert_called_once()


def test_create_application_duplicate():

    service, repo = create_service()

    repo.get_by_user_and_job.return_value = create_application()

    with pytest.raises(HTTPException):
        service.create_application(
            user_id=1,
            job_id=1,
        )


def test_get_user_applications():

    service, repo = create_service()

    applications = [create_application()]

    repo.get_by_user.return_value = applications

    result = service.get_user_applications(1)

    assert result == applications

    repo.get_by_user.assert_called_once_with(1)


def test_update_application():

    service, repo = create_service()

    application = create_application()

    repo.get_by_id_and_user.return_value = application
    repo.update.return_value = application

    updated = service.update_application(
        user_id=1,
        application_id=1,
        data=create_update_request(),
    )

    assert updated.status == "Applied"

    repo.update.assert_called_once()


def test_update_application_not_found():

    service, repo = create_service()

    repo.get_by_id_and_user.return_value = None

    result = service.update_application(
        user_id=1,
        application_id=999,
        data=create_update_request(),
    )

    assert result is None


def test_delete_application():

    service, repo = create_service()

    repo.get_by_id_and_user.return_value = create_application()

    result = service.delete_application(
        user_id=1,
        application_id=1,
    )

    assert result is True

    repo.delete.assert_called_once()


def test_delete_application_not_found():

    service, repo = create_service()

    repo.get_by_id_and_user.return_value = None

    result = service.delete_application(
        user_id=1,
        application_id=999,
    )

    assert result is False
