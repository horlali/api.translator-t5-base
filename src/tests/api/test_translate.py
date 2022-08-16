from fastapi.testclient import TestClient

from src.core.config import settings
from src.main import app

client = TestClient(app)


def test_translation(translation_payload, translation_response):
    response = client.post(
        f"{settings.API_V1_STR}/translate/", json=translation_payload
    )
    assert response.status_code == 200
    assert response.json() == translation_response


def test_translation_with_bad_payload(
    translation_bad_payload, translation_bad_payload_response
):
    response = client.post(
        f"{settings.API_V1_STR}/translate/", json=translation_bad_payload
    )
    assert response.status_code == 422
    assert response.json() == translation_bad_payload_response


def test_translation_without_payload(translation_without_payload_response):
    response = client.post(f"{settings.API_V1_STR}/translate/")
    assert response.status_code == 422
    assert response.json() == translation_without_payload_response
