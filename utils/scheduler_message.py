
import json
import datetime
from pytz import timezone

def getCurrentTime(tz):
    utc = datetime.datetime.now(datetime.timezone.utc)
    BRSP = timezone(tz)
    timeNow = utc.astimezone(BRSP)

    return timeNow


def read_reminders(file="../data/reminders.json"):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data