from fastapi.testclient import TestClient

from src.main import app
from src.core.config import settings

client = TestClient(app)


def test_translation():
    payload = {
        "source_language": "English",
        "destination_language": "French",
        "text": "How are you?",
    }
    response = client.post(f"{settings.API_V1_STR}/translate/", json=payload)
    assert response.status_code == 200
    assert response.json() == "Comment vous êtes-vous?"


def test_translation_with_wrong_payload():
    payload = {
        "source_language": "Twi",
        "destination_language": "French",
        "text": "How are you?",
    }
    response = client.post(f"{settings.API_V1_STR}/translate", json=payload)
    assert response.status_code == 404
