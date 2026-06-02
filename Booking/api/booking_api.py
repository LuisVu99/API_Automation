from api.api_client import ApiClient

class BookingAPI(ApiClient):
    def create_booking(self, payload):
        return self.post(
            "/booking",
            payload
        )
    
    def view_booking(self, booking_id):
        return self.get(f"/booking/{booking_id}")
    
    def delete_booking(self, booking_id, token=None):
        if token:
            return self.request_context.delete(
                f"/booking/{booking_id}",
                headers={"Cookie": f"token={token}"}
            )
        return self.delete(f"/booking/{booking_id}")
    
    def update_booking(self, booking_id, payload, token=None):
        if token:
            return self.request_context.put(
                f"/booking/{booking_id}",
                data = payload,
                headers = {
                    "Cookie" : f"token={token}"
                }
            )
        return self.update_booking(f"/booking/{booking_id}")
    
    def view_all_booking(self):
        return self.get("/booking")
    
    def update_partially_booking(self,booking_id,payload,  token= None):
        if token:
            return self.request_context.patch(
                f"/booking/{booking_id}",
                data=payload,
                headers = {
                    "Cookie" : f"token={token}"
                }
            )
        return self.patch(f"/booking/{booking_id}")