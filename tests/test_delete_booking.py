from api.booking_api import BookingAPI

def test_delete_booking(api_context, booking_id, get_token):

    booking_api = BookingAPI(api_context)

    response = booking_api.delete_booking(booking_id, get_token)

    assert response.status in [200, 201], f"Expected 200 or 201, but got {response.status}"
    
    print(f"✓ Booking {booking_id} deleted successfully")
