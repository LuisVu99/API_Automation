from api.booking_api import BookingAPI
from utils.config_reader import get_data

def test_update_booking(api_context, booking_id, get_token):
    body_data = get_data("booking_data")["update_booking_payload"]
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
    assert price == body_data["totalprice"], f"expected {body["totalprice"]}, but got {price}"
    
    deposit_paid = body["depositpaid"]
    assert deposit_paid == body_data["depositpaid"], f"expected depositpaid as {body["depositpaid"]}, but got {deposit_paid}"

    check_in = body["bookingdates"]["checkin"]
    assert check_in == body_data["bookingdates"]["checkin"], f"Expected '{body_data["bookingdates"]["checkin"]}', but got '{check_in}'"

    check_out = body["bookingdates"]["checkout"]
    assert check_out == body_data["bookingdates"]["checkout"], f"Expected '{body_data["bookingdates"]["checkout"]}', but got '{check_out}'"
    
    meal = body["additionalneeds"]
    assert meal == body_data["additionalneeds"], f"Expected '{body_data["additionalneeds"]}', but got '{meal}'"



