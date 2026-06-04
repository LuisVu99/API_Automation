from api.booking_api import BookingAPI
from utils.config_reader import get_data

def test_get_a_booking(api_context, booking_id):
    booking_api = BookingAPI(api_context)
    response = booking_api.view_booking(booking_id)
    # body = response.json()
    first_name = response.json()["firstname"]
    assert response.status == 200
    assert first_name == get_data("booking_data")["create_booking_payload_batch_2"]["firstname"]
    print(response.status)
    print(response.json())
    print(booking_id)

