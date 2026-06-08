import uuid

def generate_tracking_id():
    return "TRK-" + str(uuid.uuid4())[:8].upper()