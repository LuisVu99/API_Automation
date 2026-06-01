from api.booking_api import BookingAPI

def test_get_a_booking(api_context):
    booking_api = BookingAPI(api_context)
    response = booking_api.view_booking("2783")
    # # body = response.json()
    # first_name = body["firstname"]
    assert response.status == 200
    # assert first_name == "Luis"

