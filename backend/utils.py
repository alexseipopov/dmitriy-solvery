def create_response(status="SUCCESS", code=0, description="OK", data=None):
    if data is None:
        data = {}
    return {
            "status": status,
            "code": code,
            "description": description,
            "data": data
        }