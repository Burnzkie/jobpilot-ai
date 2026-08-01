from pydantic import BaseModel


class ResumeResponse(BaseModel):

    id: int

    filename: str

    original_filename: str

    extracted_text: str | None

    model_config = {"from_attributes": True}
