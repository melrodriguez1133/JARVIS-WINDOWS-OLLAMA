from datetime import datetime


def get_time():
    now = datetime.now()
    return f"La hora actual es {now.strftime('%H:%M:%S')}"