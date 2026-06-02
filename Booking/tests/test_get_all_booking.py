from api.booking_api import BookingAPI

def test_get_all_booking(api_context, booking_id):
    booking_api = BookingAPI(api_context)
    response = booking_api.view_all_booking()
    assert response.status in [200, 201]
    body = response.json()
    booking_ids = [booking["bookingid"] for booking in body]
    assert booking_id in booking_ids, f"Expected {booking_id} in response, but got {booking_ids}"