from api.booking_api import BookingAPI
from utils.config_reader import get_data

def test_update_booking(api_context, booking_id, get_token):
    body_data = get_data("booking_data")["update_booking_payload_batch_2"]
    booking_api = BookingAPI(api_context)
    response = booking_api.update_booking(booking_id, body_data, get_token)
    assert response.status == 200
    body = response.json()

    first_name = body["firstname"]
    assert first_name == body_data["firstname"]

    last_name = body["lastname"]
    assert last_name == body_data["lastname"]

    price = body["totalprice"]
    assert price > 0
    assert price == body_data["totalprice"]
    
    deposit_paid = body["depositpaid"]
    assert deposit_paid == body_data["depositpaid"]

    check_in = body["bookingdates"]["checkin"]
    assert check_in == body_data["bookingdates"]["checkin"]

    check_out = body["bookingdates"]["checkout"]
    assert check_out == body_data["bookingdates"]["checkout"]
    
    meal = body["additionalneeds"]
    assert meal == body_data["additionalneeds"]


