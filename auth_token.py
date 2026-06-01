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
            "Content-Type" : "application/json"
        }
    )
    response = request_context.post("/auth", data=credentials)
    body = response.json()
    print (body)
    print (response.status)