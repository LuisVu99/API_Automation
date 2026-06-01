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