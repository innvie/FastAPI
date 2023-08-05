import requests
import urllib3
from datetime import datetime
import ssl

urllib3.disable_warnings()  # This will disable SSL warnings


def get_access_token_info():
    url = "https://euapi.sciener.com/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "clientId": "7ee9c51bc0134e0585c7e4ebf46701fc",
        "clientSecret": "9739624c25d7ab454c67843d49aff20c",
        "username": "h_1690163127687",
        "password": "3740c0567ca4aa864141adf1dae9582b",
    }

    response = requests.post(
        url, headers=headers, data=data, verify=False
    )  # Set verify=False to disable SSL verification

    if response.status_code == 200:
        access_token_info = response.json()
        if access_token_info:
            access_token_info["current_date"] = datetime.now().isoformat()
            print("Successfully added access token to database")
        else:
            print("Failed to get access token")
            access_token_info.error_state = True
            access_token_info.error_message = "Failed to get access token"
            return access_token_info.json()
        print(response.json())
        return response.json()
    else:
        print(f"Failed to get access token. Status code: {response.status_code}")
        return None


def get_access_token():
    access_token_info = get_access_token_info()
    if access_token_info:
        access_token = access_token_info.get("access_token")
        print("Access Token:", access_token)
    return access_token
