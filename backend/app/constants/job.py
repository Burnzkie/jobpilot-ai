from enum import StrEnum


class JobStatus(StrEnum):
    SAVED = "Saved"
    APPLIED = "Applied"
    INTERVIEW = "Interview"
    OFFER = "Offer"
    REJECTED = "Rejected"


DEFAULT_JOB_SCORE = 0
