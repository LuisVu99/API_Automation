def get_token(api_context):
    response = api_context.post(
        "/auth",
        data = {
            "username" : "admin",
            "password" : "password123"
        }
    )
    assert response.status == 200, f"Expected 200, but got {response.status}"
    print(response.status)
    return response.json()["token"]
    