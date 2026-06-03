import pytest
from playwright.sync_api import sync_playwright
from utils.config_reader import get_config, get_data

@pytest.fixture
def api_context():
    config = get_config("dev")
    with sync_playwright() as p:
        context = p.request.new_context(
            base_url=config["url"]
        )
        yield context
        context.dispose()

@pytest.fixture
def get_token(api_context):
    config = get_config("dev")
    response = api_context.post(
        "/auth",
        data=config["credentials"]
    )
    assert response.status == 200
    return response.json()["token"]

@pytest.fixture
def booking_id(api_context):
    data = get_data("booking_data")
    response = api_context.post(
        "/booking",
        data= data["create_booking_payload_batch_2"]
    )
    return response.json()["bookingid"]