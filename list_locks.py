"""module to get and format list of locks registered"""
import json
import requests
import urllib3
from date_param import get_date_param

urllib3.disable_warnings(category = urllib3.exceptions.InsecureRequestWarning)

# Create a session and configure it to not verify SSL certificates
session = requests.Session()
session.verify = False

# Base URL for the API
BASE_URL = "https://euapi.sciener.com/v3/lock/listByHotel"
CLIENT_ID = "7ee9c51bc0134e0585c7e4ebf46701fc"


def get_list_locks(access_token):
    """function to get a list of lock objects with innvie data"""
    date_param = get_date_param()
    params = {
        "clientId": CLIENT_ID,
        "accessToken": access_token,
        "pageNo": 1,
        "pageSize": 20,
        "date": date_param,
        "groupId": 1719,
    }
    # Disable SSL certificate verification for this specific request
    response = session.get(BASE_URL, params=params, verify=False)
    # Check the response status code
    if response.status_code == 200:
        # Request successful
        data = response.json()
        formatted_json = json.dumps(data, indent=2)
        # print(formatted_json)
        return data
    else:
        # Request failed
        print(f"Error: {response.status_code} - {response.text}")
        return None


def get_all_lock_ids(access_token):
    """function to get a list of all locks, just id's"""
    data = get_list_locks(access_token)
    if data is None:
        return None
    lock_ids = [item["lockId"] for item in data["list"]]
    return lock_ids


def get_lock_id_for_room(access_token, room_no):
    """Retrieve the ID of a specific room number."""
    data = get_list_locks(access_token)
    if data is None:
        print("no locks found")
        return None

    for item in data['list']:
        if item['lockAlias'] == room_no:
            lock_id = item['lockId']
            return lock_id

    # Return None if the room number is not found
    return None
