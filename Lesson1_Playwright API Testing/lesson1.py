from playwright.sync_api import sync_playwright
import time
# #1. Request context
# with sync_playwright() as p:
#     request_context = p.request.new_context()
#     response = request_context.get("https://restful-booker.herokuapp.com/booking")
#     print (response.status)

#     response2 = request_context.get("https://restful-booker.herokuapp.com/booking/1")
#     body = response2.json()
#     print(body)

# #1.HW1: GET https://reqres.in/api/users/2
with sync_playwright() as p:
    url = "https://restful-booker.herokuapp.com/booking/1"
    request_context = p.request.new_context()
    response = request_context.get(url)
    body = response.json()
    print(body)
    assert response.status == 200

    assert body["totalprice"] == 640

    assert "Susan" in body["firstname"], f"firstname does not include 'Mark'"

    start = time.time()
    response = request_context.get(url)
    end= time.time()
    response_time = end - start
    assert response_time < 3, f"Expected response_time < 3, but got {response_time:.3f}"

#2. HW 2
with sync_playwright() as p:
    url = "https://restful-booker.herokuapp.com/booking"
    payload = {
        "firstname":"Luis",
        "lastname":"Vu",
        "totalprice":2000,
        "depositpaid": True,
        "bookingdates":{
            "checkin":"2025-05-12",
            "checkout":"2025-06-14",
        },
        "additionalneeds":"Breakfast"
    }
    request_context = p.request.new_context()
    response = request_context.post(url, data=payload)
    body = response.json()
    first_name_actual = body["booking"]["firstname"]
    last_name_actual = body["booking"]["lastname"]
    checkin_actual = body["booking"]["bookingdates"]["checkin"]
    print (body)
    assert (response.status) == 200, f"Expect 200, but got {response.status}"
    assert first_name_actual == "Luis", f"Expect Luis, but got {first_name_actual}"
    assert last_name_actual == "Vu", f"Expect Vu, but got {last_name_actual}"
    assert checkin_actual == "2025-05-12", f"Expect 2025-05-12, but got {checkin_actual}"
    assert "firstname" in body["booking"], f"Expect existing, but do not exist firstname"
    assert "checkout" in body["booking"]["bookingdates"], f"Expect existing, but do not exist checkout"
