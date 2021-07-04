import pytest
import requests


URL = "https://deckofcardsapi.com/api/deck/new/shuffle/"


@pytest.fixture
def response_and_json():
    response = requests.post(URL, data={"deck_count": 1})
    json_data = response.json()
    yield response, json_data

