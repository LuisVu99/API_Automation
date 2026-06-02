from api.booking_api import BookingAPI
from utils.config_reader import get_data

def test_create_booking(api_context):
    body_data = get_data("booking_data")["create_booking_payload"]
    booking_api = BookingAPI(api_context)
    response = booking_api.create_booking(body_data)
    assert response.status == 200, f"Expected 200, but got {response.status}"
    body = response.json()
    assert body["bookingid"] > 0
    print(f"✓ Booking created with ID: {body['bookingid']}")
    print(body)
