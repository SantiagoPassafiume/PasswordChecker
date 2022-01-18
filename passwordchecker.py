import requests
import hashlib


def request_api_data(query_chars):
    url = f"https://api.pwnedpasswords.com/range/{query_chars}"
    response = requests.get(url)
    status = response.status_code
    if status != 200:
        raise RuntimeError(f"Error fetching: {status}")
    return response


def check_password(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_5_chars, remaining_chars = sha1_password[:5], sha1_password[5:]
    return sha1_password


# request_api_data("123")
