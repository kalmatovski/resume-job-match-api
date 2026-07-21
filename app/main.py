from fastapi import FastAPI

from app.matching import create_match_result
from app.schemas import MatchRequest, MatchResponse

app = FastAPI()

@app.post("/match", response_model=MatchResponse)
def match_resume(request:MatchRequest) -> MatchResponse:
    result = create_match_result(resume=request.resume_text,
                                 job=request.job_description)
    
    return MatchResponse(**result)