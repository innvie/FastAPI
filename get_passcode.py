"""Module to create passcodes for the locks"""
import os
import requests
from get_token import get_access_token
from list_locks import get_lock_id_for_room
from timestamp import (
    convert_string_startdate_to_milliseconds,
    convert_string_enddate_to_milliseconds,
    get_timestamp_milliseconds,
)


def get_access_passcode(token, room_no, start_date, end_date):
    """gets passcode for a specific room on specific date"""
    access_token = get_access_token()
    lock_id = get_lock_id_for_room(access_token, room_no)
    integer_timestamp = get_timestamp_milliseconds()

    start_date = convert_string_startdate_to_milliseconds(start_date)
    end_date = convert_string_enddate_to_milliseconds(end_date)
    date = integer_timestamp

    data = {
        "clientId": os.environ["CLIENT_ID"],
        "clientSecret": os.environ.get("CLIENT_SECRET"),
        "username": os.environ.get("USERNAME"),
        "password": os.environ.get("PASSWORD"),
        "accessToken": token,
        "lockId": lock_id,
        "keyboardPwdType": os.environ.get("KEYBOARD_PWD_TYPE"),
        "startDate": start_date,
        "endDate": end_date,
        "date": date,
    }
    print("data")
    print(data)

    try:
        response = requests.post(os.environ.get("API_URL"), data=data, verify=False, timeout=10)
        response.raise_for_status()  # Raise exception if the response status is not 2xx
        result = response.json()
        print("result:", result)
        passcode = result.get("keyboardPwd")
        return passcode
    except requests.exceptions.ConnectionError as connection_error:
        print("An error occurred during the request:", connection_error)
    except ValueError as value_error:
        print("Failed to parse JSON response:", value_error)
    return None
