from pydantic import BaseModel, Field

class MatchRequest(BaseModel):
    resume_text: str = Field(min_length=10)
    job_description: str = Field(min_length=10)


class MatchResponse(BaseModel):
    match_score: float
    matched_skills: list[str]
    missing_skills: list[str]
    fit_level: str
    recommendation: str