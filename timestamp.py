import datetime
import pytz


def current_time():
    # Set the time zone to Mexico City (Central Daylight Time - CDT)
    mexico_city_tz = pytz.timezone("America/Mexico_City")
    time = datetime.datetime.now(mexico_city_tz)
    return time


def get_timestamp_milliseconds():
    mx_time = current_time()
    timestamp_milliseconds = int(mx_time.timestamp() * 1000)
    return timestamp_milliseconds


def string_to_date(date_string):
    return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()


def convert_string_date_to_milliseconds(date):
    mx_date = string_to_date(date)
    mx_datetime = datetime.datetime.combine(
        mx_date, datetime.datetime.min.time()
    )  # Combine with midnight time
    timestamp_milliseconds = int(mx_datetime.timestamp() * 1000)
    return timestamp_milliseconds
