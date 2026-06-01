from api.booking_api import BookingAPI
from api.auth_api import get_token

def test_delete_booking(api_context):
    # Lấy token
    token = get_token(api_context)
    
    booking_api = BookingAPI(api_context)
    response = booking_api.delete_booking("2783", token=token)
    assert response.status in [200, 201], f"Expected 200 or 201, but got {response.status}"
    print(f"✓ Booking 4363 deleted successfully")
