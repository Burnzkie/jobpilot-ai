from unittest.mock import Mock, patch

from app.constants.job import DEFAULT_JOB_SCORE
from app.models.job import Job
from app.models.resume import Resume
from app.services.matching_service import MatchingService


def create_service():
    repo = Mock()
    service = MatchingService(repo)
    return service, repo


def create_resume():
    return Resume(
        id=1,
        extracted_text="Python FastAPI SQL",
        user_id=1,
    )


def create_job():
    return Job(
        id=1,
        description="Python FastAPI Developer",
    )


@patch("app.services.matching_service.calculate_ai_score")
def test_score_job(mock_score):

    service, repo = create_service()

    repo.get_latest_by_user.return_value = create_resume()

    mock_score.return_value = {
        "overall": 95,
    }

    score = service.score_job(
        1,
        create_job(),
    )

    assert score == 95

    repo.get_latest_by_user.assert_called_once_with(1)


def test_score_job_without_resume():

    service, repo = create_service()

    repo.get_latest_by_user.return_value = None

    score = service.score_job(
        1,
        create_job(),
    )

    assert score == DEFAULT_JOB_SCORE
