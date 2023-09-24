import json
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


valid_token = "valid_token_here"


def test_create_guidance():
    guidance_data = {
        "query": "How does GDPR Article 1 apply to data processing?",
        "context": 1
    }
    response = client.post("/generate-guide", json=guidance_data, headers={"Authorization": f"Bearer {valid_token}"})
    assert response.status_code == 200
    data = response.json()
    assert "arti_number" in data
    assert "response" in data
