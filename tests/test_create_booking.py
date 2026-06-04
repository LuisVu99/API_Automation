from api.booking_api import BookingAPI
from utils.config_reader import get_data
import pytest

payloads = get_data("booking_data")["create_booking_payload"]

@pytest.mark.parametrize("payload", payloads)
def test_create_booking(api_context, payload):
    booking_api = BookingAPI(api_context)
    response = booking_api.create_booking(payload)
    assert response.status == 200, f"Expected 200, but got {response.status}"
    body = response.json()
    assert body["bookingid"] > 0
    print(f"✓ Booking created with ID: {body['bookingid']}")
    print(body)

    first_name = body["booking"]["firstname"]
    assert first_name == payload["firstname"], f"expected {first_name}, but got {payloads["firstname"]}"

    last_name = body["booking"]["lastname"]
    assert last_name == payload["lastname"]

    price = body["booking"]["totalprice"]
    assert price > 0
    assert price == payload["totalprice"], f"expected {body["totalprice"]}, but got {price}"
    
    deposit_paid = body["booking"]["depositpaid"]
    assert deposit_paid == payload["depositpaid"], f"expected depositpaid as {body["depositpaid"]}, but got {deposit_paid}"

    check_in = body["booking"]["bookingdates"]["checkin"]
    assert check_in == payload["bookingdates"]["checkin"], f"Expected '{payload["bookingdates"]["checkin"]}', but got '{check_in}'"

    check_out = body["booking"]["bookingdates"]["checkout"]
    assert check_out == payload["bookingdates"]["checkout"], f"Expected '{payload["bookingdates"]["checkout"]}', but got '{check_out}'"
    
    meal = body["booking"]["additionalneeds"]
    assert meal == payload["additionalneeds"], f"Expected '{payload["additionalneeds"]}', but got '{meal}'"




