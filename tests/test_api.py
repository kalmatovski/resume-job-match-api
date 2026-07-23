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

    