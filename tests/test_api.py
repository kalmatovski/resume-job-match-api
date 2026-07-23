from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_match_success():
    request_data = {
    "resume_text": "Python pandas scikit-learn FastAPI",
    "job_description": "Python SQL Docker FastAPI ML pipelines"
}
    response = client.post("/match", json=request_data)

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["match_score"] == 0.226
    assert response_data["matched_skills"] == ["fastapi", "python"]
    assert response_data["missing_skills"] == ["docker", "sql"]
    assert response_data["fit_level"] == "low"
    assert "docker" in response_data["recommendation"]
    assert "sql" in response_data["recommendation"]

def test_match_missing_resume_text():
    request_body = {
        "job_description":"Python SQL Docker"
    }

    response = client.post("/match",json=request_body)

    assert response.status_code == 422

def test_match_empty_resume_text():
    request_data = {
        "resume_text": "",
        "job_description": "Python SQL Docker FastAPI ML pipelines"
    }

    response = client.post(
        "/match",
        json=request_data
    )

    assert response.status_code == 422
