from api.booking_api import BookingAPI
from utils.config_reader import get_data, get_config

def test_take_token(api_context):
    # Get token
    config = get_config("dev")
    create_body = get_data("booking_data")["create_booking_payload"]
    update_body = get_data("booking_data")["update_booking_payload"]
    take_token_response = api_context.post(
        "/auth",
        data = config["credentials"]
    )
    token = take_token_response.json()["token"]
    assert take_token_response.status in[200, 201]

    # Create booking
    body_data = create_body
    booking_api = BookingAPI(api_context)
    create_booking_response = booking_api.create_booking(body_data)
    assert create_booking_response.status in[200, 201]
    booking_id = create_booking_response.json()["bookingid"]

    # Get booking
    get_booking_response = booking_api.view_booking(booking_id)
    assert get_booking_response.status in [200, 201]

    # Update booking
    update_body_data = update_body
    update_booking_response = booking_api.update_booking(booking_id, update_body_data, token)
    assert update_booking_response.status in [200, 201]

    # Delete booking
    delete_booking_response = booking_api.delete_booking(booking_id, token)
    assert delete_booking_response.status in [200, 201]