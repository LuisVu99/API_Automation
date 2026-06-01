from api.booking_api import BookingAPI

def test_create_booking(api_context):
    booking_api = BookingAPI(api_context)
    response = booking_api.create_booking(
        {
            "firstname":"Luis",
            "lastname":"Vu",
            "totalprice":2000,
            "depositpaid":True,
            "bookingdates":{
                "checkin":"2025-05-12",
                "checkout":"2025-06-14"
            },
            "additionalneeds":"Breakfast"
        }
    )
    assert response.status == 200, f"Expected 200, but got {response.status}"
    body = response.json()
    assert body["bookingid"] > 0
    print(f"✓ Booking created with ID: {body['bookingid']}")
