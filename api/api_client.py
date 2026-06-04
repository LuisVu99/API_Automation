class ApiClient:
    def __init__(self, request_context):
        self.request_context = request_context

    def get(self, endpoint):
        return self.request_context.get(endpoint)
    
    def post(self, endpoint, payload):
        return self.request_context.post(
            endpoint,
            data = payload
        )
    
    def put(self, endpoint, payload):
        return self.request_context.put(
            endpoint,
            data= payload
        )
    
    def patch(self, endpoint, payload):
        return self.request_context.patch(
            endpoint,
            data=payload
        )
    
    def delete(self, endpoint):
        return self.request_context.delete(endpoint)