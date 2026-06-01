from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    base_url = "https://restful-booker.herokuapp.com"
    credentials = {
        "username" : "admin",
        "password" : "password123"
    }
    request_context = p.request.new_context(
        base_url = base_url,
        extra_http_headers= {
            "Content-Type" : "application/json",
            "Accept": "application/json"
        }
    )
    response = request_context.post("/auth", data=credentials)
    body = response.json()
    token = body["token"]
    assert response.status == 200
    assert "token" in body, f"Expected to display token, but display {body}"

    #2.Post request
    body_data = {
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
    response_create_booking = request_context.post(
        "/booking",
        headers= {
            "Cookie" : f"token={token}"
        },
        data= body_data
    )
    body_create_booking = response_create_booking.json()
    id = body_create_booking["bookingid"]
    first_name = body_create_booking["booking"]["firstname"]
    last_name = body_create_booking["booking"]["lastname"]
    price = body_create_booking["booking"]["totalprice"]
    deposit_paid = body_create_booking["booking"]["depositpaid"]
    meal = body_create_booking["booking"]["additionalneeds"]
    check_in = body_create_booking["booking"]["bookingdates"]["checkin"]
    check_out = body_create_booking["booking"]["bookingdates"]["checkout"]
    assert id > 0
    assert first_name == body_data["firstname"], f"expected {body_data["firstname"]},but got {first_name}"
    assert "Vu" in last_name, f"expected last name include Vu, but got {last_name}"
    assert 0 <= price <= 2000
    assert deposit_paid == True, f"Expected deposit_paid as True, but got {deposit_paid}"
    assert meal == body_data["additionalneeds"], f"Expected breakfast, but got {meal}"
    assert check_in == body_data["bookingdates"]["checkin"], f"Expected {body_data["bookingdates"]["checkin"]}, but got {check_in}"
    assert check_out == body_data["bookingdates"]["checkout"], f"Expected {body_data["bookingdates"]["checkout"]}, but got {check_out}"

    #3. Put request
    update_body_data = {
            "firstname":"linh",
            "lastname":"Le",
            "totalprice":2000,
            "depositpaid":True,
            "bookingdates":{
                "checkin":"2025-05-12",
                "checkout":"2025-06-14"
            },
            "additionalneeds":"Breakfast"
    }
    response_update_booking = request_context.put(
        f"/booking/{id}",
        headers= {
            "Cookie" : f"token={token}"
        },
        data = update_body_data
    )
    body_update_booking = response_update_booking.json()
    # print (response_update_booking.status)
    # print (body_update_booking)
    assert response_update_booking.status == 200

    #3. Patch request
    update_partially_body_data = {
            "firstname":"Lona",
            # "lastname":"Le",
            "totalprice":1000,
            # "depositpaid":False,
            "bookingdates":{
                "checkin":"2025-10-12",
                "checkout":"2025-06-14"
            },
            # "additionalneeds":"Breakfast"
    }
    request_update_partially_booking = request_context.patch(
        f"/booking/{id}",
        headers= {
            "Cookie" : f"token={token}"
        },
        data = update_partially_body_data
    )
    response_update_partially_booking = request_update_partially_booking.json()
    assert request_update_partially_booking.status == 200
    # print(response_update_partially_booking)

    #4. Get all booking
    request_get_all_booking = request_context.get("/booking")
    response_all_booking = request_get_all_booking.json()
    booking_ids = [booking["bookingid"] for booking in response_all_booking]
    assert id in booking_ids, f"Expected booking id {id} to be in the list, but got {booking_ids}"

    #5. Delete a booking
    request_delete_booking = request_context.delete(
        f"/booking/{id}",
        headers={
            "Cookie" : f"token={token}"
        }
    )
    assert request_delete_booking.status in [200, 201], f"Expected 200 or 201, but got {request_delete_booking.status}"
    assert "Created" in request_delete_booking.text(), f"Expected Created, but got {request_delete_booking.text()}"

    #6. Verify user deleted successfully
    request_get_a_booking_deleted = request_context.get(
        f"/booking/{id}"
    )
    assert request_get_a_booking_deleted.status == 404, f"Expected 404,but got {request_get_a_booking_deleted.status} status"