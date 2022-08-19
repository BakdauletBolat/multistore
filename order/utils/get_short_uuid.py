import uuid

def get_short_uuid():
        return str(uuid.uuid4())[:10]