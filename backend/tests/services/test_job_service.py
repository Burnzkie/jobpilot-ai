from unittest.mock import Mock

import pytest

from app.constants.job import DEFAULT_JOB_SCORE, JobStatus
from app.core.exceptions import DuplicateResourceException, NotFoundException
from app.models.job import Job
from app.services.job_service import JobService


def create_service():
    repo = Mock()
    matcher = Mock()

    service = JobService(
        repo=repo,
        matcher=matcher,
    )

    return service, repo, matcher


def create_job():
    return Job(
        id=1,
        title="Backend Developer",
        company="OpenAI",
        location="Remote",
        salary="$5000",
        description="Python FastAPI",
        url="https://job.test",
        source="LinkedIn",
        status=JobStatus.SAVED,
        score=DEFAULT_JOB_SCORE,
        user_id=1,
    )


def create_request():
    return Mock(
        title="Backend Developer",
        company="OpenAI",
        location="Remote",
        salary="$5000",
        description="Python FastAPI",
        url="https://job.test",
        source="LinkedIn",
    )


def test_create_job():

    service, repo, matcher = create_service()

    repo.get_by_user_and_url.return_value = None
    matcher.score_job.return_value = 92

    data = create_request()

    job = service.create_job(
        data=data,
        user_id=1,
    )

    assert job.title == "Backend Developer"
    assert job.score == 92

    repo.create.assert_called_once()


def test_create_job_duplicate_url():

    service, repo, matcher = create_service()

    repo.get_by_user_and_url.return_value = create_job()

    with pytest.raises(DuplicateResourceException):
        service.create_job(
            create_request(),
            1,
        )


def test_get_job():

    service, repo, matcher = create_service()

    repo.get_by_user_and_id.return_value = create_job()

    job = service.get_job(
        1,
        1,
    )

    assert job.id == 1


def test_get_job_not_found():

    service, repo, matcher = create_service()

    repo.get_by_user_and_id.return_value = None

    with pytest.raises(NotFoundException):
        service.get_job(
            1,
            999,
        )


def test_update_job():

    service, repo, matcher = create_service()

    job = create_job()

    repo.get_by_user_and_id.return_value = job

    data = Mock()

    data.model_dump.return_value = {
        "title": "Senior Backend Developer",
    }

    updated = service.update_job(
        1,
        1,
        data,
    )

    assert updated.title == "Senior Backend Developer"

    repo.update.assert_called_once()


def test_delete_job():

    service, repo, matcher = create_service()

    repo.get_by_user_and_id.return_value = create_job()

    result = service.delete_job(
        1,
        1,
    )

    assert result is True

    repo.delete.assert_called_once()


def test_delete_job_not_found():

    service, repo, matcher = create_service()

    repo.get_by_user_and_id.return_value = None

    with pytest.raises(NotFoundException):
        service.delete_job(
            1,
            999,
        )


def test_change_status():

    service, repo, matcher = create_service()

    job = create_job()

    repo.get_by_user_and_id.return_value = job

    updated = service.change_status(
        1,
        1,
        JobStatus.APPLIED,
    )

    assert updated.status == JobStatus.APPLIED

    repo.update.assert_called_once()


def test_get_jobs():

    service, repo, matcher = create_service()

    jobs = [create_job()]

    repo.get_by_user.return_value = jobs

    result = service.get_jobs(1)

    assert result == jobs

    repo.get_by_user.assert_called_once_with(1)


def test_update_job_not_found():

    service, repo, matcher = create_service()

    repo.get_by_user_and_id.return_value = None

    data = Mock()

    with pytest.raises(NotFoundException):
        service.update_job(
            1,
            999,
            data,
        )
