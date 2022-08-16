import pytest


@pytest.fixture
def translation_payload():
    return {
        "source_language": "English",
        "destination_language": "French",
        "text": "How are you?",
    }


@pytest.fixture
def translation_response():
    return "Comment vous êtes-vous?"


@pytest.fixture
def translation_bad_payload():
    return {
        "source_language": "Twi",
        "destination_language": "French",
        "text": "How are you?",
    }


@pytest.fixture
def translation_bad_payload_response():
    return {
        "detail": [
            {
                "loc": ["body", "source_language"],
                "msg": "value is not a valid enumeration member; permitted: 'English', 'French', 'German', 'Romanian'",  # noqa: E501
                "type": "type_error.enum",
                "ctx": {"enum_values": ["English", "French", "German", "Romanian"]},
            }
        ]
    }


@pytest.fixture
def translation_without_payload_response():
    return {
        "detail": [
            {"loc": ["body"], "msg": "field required", "type": "value_error.missing"}
        ]
    }
