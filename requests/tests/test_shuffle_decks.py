import requests

from cerberus import Validator
from assertpy import assert_that


API_URL = "https://deckofcardsapi.com/api/deck"


def test_json_data_has_valid_schema(response_and_json):
    schema = {
        "success": {"type": "boolean"},
        "deck_id": {"type": "string"},
        "shuffled": {"type": "boolean"},
        "remaining": {"type": "number"}
    }
    validator = Validator(schema, require_all=True)

    _, json_data = response_and_json

    is_valid = validator.validate(json_data)
    assert_that(is_valid, description=validator.errors).is_true()


def test_status_is_success(response_and_json):
    _, json_data = response_and_json
    assert json_data["success"]


def test_deck_id_is_usable(response_and_json):
    deck_id = response_and_json[1]["deck_id"]
    response = requests.post(f"{API_URL}/{deck_id}/shuffle")
    assert response.json()["success"]

