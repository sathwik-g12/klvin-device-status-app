from datetime import datetime, timezone, timedelta

def get_device_status(last_reading_time):
    if last_reading_time is None:
        return "offline"
    now = datetime.now(timezone.utc)
    if (now - last_reading_time) <= timedelta(minutes=2):
        return "online"
    return "offline"
