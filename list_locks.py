import requests
import json
from date_param import get_date_param

requests.packages.urllib3.disable_warnings()

# Base URL for the API
base_url = "https://euapi.sciener.com/v3/lock/listByHotel"
client_id = "7ee9c51bc0134e0585c7e4ebf46701fc"


def get_list_locks(access_token):
    date_param = get_date_param()
    params = {
        "clientId": client_id,
        "accessToken": access_token,
        "pageNo": 1,
        "pageSize": 20,
        "date": date_param,
        "groupId": 1719,
    }
    # Disable SSL certificate verification for this specific request
    response = requests.get(base_url, params=params, verify=False)
    # Check the response status code
    if response.status_code == 200:
        # Request successful
        data = response.json()
        formatted_json = json.dumps(data, indent=2)
        print(formatted_json)
        return data
    else:
        # Request failed
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_lock_id(access_token, room_number):
    data = get_list_locks(access_token)
    if data is None:
        return None
    lock_ids = [item["lockId"] for item in data["list"]]
    return lock_ids
