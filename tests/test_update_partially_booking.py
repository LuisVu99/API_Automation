from api.booking_api import BookingAPI
from utils.config_reader import get_data

def test_update_partially_booking(api_context, booking_id, get_token):
    booking_api = BookingAPI(api_context)
    body_data = get_data("booking_data")["update_partially_booking_payload"]
    response = booking_api.update_partially_booking(
        booking_id,
        body_data,
        get_token
    )
    assert response.status in [200, 201]
    body = response.json()
    first_name = body["firstname"]
    last_name = body["lastname"]
    assert first_name == body_data["firstname"] 
    assert last_name == body_data["lastname"]