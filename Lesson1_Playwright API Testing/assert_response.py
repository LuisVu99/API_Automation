from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    request_context = p.request.new_context()
    response = request_context.post(
        "https://restful-booker.herokuapp.com/booking",
        data= {
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
    body = response.json()
    first_name = body["booking"]["firstname"]
    last_name = body["booking"]["lastname"]
    price = body["booking"]["totalprice"]
    deposit_paid = body["booking"]["depositpaid"]
    #1. Assert status code
    assert response.status == 200, f"Expected 200, but got {response.status}"
    assert response.status in [200, 201]  # Nhieu status hop le
    assert response.status < 500           # Ko duoc loi sever
    print (response.status)
    print (body)

    #2. Response body assertion
    assert first_name == "Luis", f"Expected Luis, but got {first_name}"  # Verify bang
    assert last_name != "Lan", f"Expected last name different from Lan, but got {last_name}"   # Verify khac        
    assert "Lu" in first_name   # Verify chua chuoi 
    assert first_name.startswith("Lu")    # Verify bat dau bang
    assert first_name.endswith("is")   #Verify ket thuc bang

    #3 Verify key ton tai
    assert "bookingid" in body, f"expected bookingid, but bookingid not exist"
    assert "firstname" in body["booking"]  #Nested JSON

    expected_keys = [
        "firstname",
        "lastname",
        "totalprice"
    ]
    for key in expected_keys:
        assert key in body["booking"], f"expected include firstname, lastname, total price, but got {body}"   #Nhieu keys

    #4. Verify data type
    #String, integer, boolean, list
    assert isinstance(first_name, str)
    assert isinstance(price, int)
    assert isinstance(deposit_paid, bool)
    assert isinstance(body, dict), f"expected body as list, but got {type(body)}"

    #5 Verify null/not null
    assert first_name is not None   #Not null
    # assert body["error"] is None    # Error phai null

    # #6. Verify Number Range
    assert price > 0
    assert price < 1000, f"expected price in range from 0 to 1000, but got {price}"
    assert 0 <= price <= 2000, f"expected price in range from 0 to 1000, but got {price}"  # Trong khoang 0 den 1000

    # #7. Verify List
    # user = {
    #         "users":[
    #             {"name":"Luis"},
    #             {"name":"Tom"}
    #         ]
    #         }
    # assert len(body["users"]) > 0  #Verify list ko rong
    # assert len(body["users"]) == 2   #Verify so luong phan tu

    # names = [
    #     user["name"]
    #     for user in body["users"]
    # ]
    # assert "Luis" in names   #Verify item trong list ton tai