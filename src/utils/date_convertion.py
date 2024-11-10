import datetime

# Convert to UTC or remove timezone
def make_timezone_naive(dt):
    if dt.tzinfo is not None:
        return dt.astimezone(datetime.timezone.utc).replace(tzinfo=None)
    return dt