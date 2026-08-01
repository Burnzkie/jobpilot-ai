from app.ai.cover_letter import generate_cover_letter


class CoverLetterService:

    def create(
        self,
        data,
    ):
        return generate_cover_letter(
            name=data.name,
            job_title=data.job_title,
            company=data.company,
            resume_skills=data.resume_skills,
            job_description=data.job_description,
        )
