from datetime import datetime


def get_date_param():
    # Get the current timestamp in milliseconds
    current_timestamp = int(datetime.now().timestamp() * 1000)

    # Calculate the timestamp for 5 minutes from now
    five_minutes_from_now = current_timestamp + 5 * 60 * 1000

    # Calculate the timestamp for 5 minutes ago
    five_minutes_ago = current_timestamp - 5 * 60 * 1000

    # Replace this value with the desired 'date' parameter (in milliseconds) or keep it as None
    date_param = None

    # Check if the 'date' parameter is missing or not a valid number
    if not date_param or not isinstance(date_param, int):
        # Set the 'date' parameter to the current timestamp
        date_param = current_timestamp

    # Check if the 'date' parameter value is within the valid range
    if date_param < five_minutes_ago or date_param > five_minutes_from_now:
        # Set the 'date' parameter to the current timestamp
        date_param = current_timestamp

    return date_param
