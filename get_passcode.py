import requests
import datetime
import ssl
from timestamp import (
    convert_string_startdate_to_milliseconds,
    convert_string_enddate_to_milliseconds,
    get_timestamp_milliseconds,
)


def get_access_passcode(token, roomNo, startDate, endDate):
    api_url = "https://euapi.sciener.com/v3/keyboardPwd/get"
    client_id = "7ee9c51bc0134e0585c7e4ebf46701fc"
    client_secret = "9739624c25d7ab454c67843d49aff20c"
    username = "h_1690163127687"
    password = "3740c0567ca4aa864141adf1dae9582b"
    access_token = token
    lock_id = 5712887
    keyboard_pwd_type = 3

    integer_timestamp = get_timestamp_milliseconds()

    start_date = convert_string_startdate_to_milliseconds(startDate)
    end_date = convert_string_enddate_to_milliseconds(endDate)
    date = integer_timestamp

    data = {
        "clientId": client_id,
        "clientSecret": client_secret,
        "username": username,
        "password": password,
        "accessToken": access_token,
        "lockId": lock_id,
        "keyboardPwdType": keyboard_pwd_type,
        "startDate": start_date,
        "endDate": end_date,
        "date": date,
    }

    try:
        response = requests.post(api_url, data=data, verify=False)
        response.raise_for_status()  # Raise exception if the response status is not 2xx
        result = response.json()
        print("result:", result)
        passcode = result.get("keyboardPwd")
        return passcode
    except requests.exceptions.RequestException as e:
        print("An error occurred during the request:", e)
    except ValueError as ve:
        print("Failed to parse JSON response:", ve)
    except Exception as ex:
        print("Unexpected error occurred:", ex)
    return None
