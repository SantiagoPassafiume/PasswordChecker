import requests


def request_api_data(query_chars):
    url = f"https://api.pwnedpasswords.com/range/{query_chars}"
    response = requests.get(url)
    status = response.status_code
    if status != 200:
        raise RuntimeError(f"Error fetching: {status}")
    return response


def check_password(password):
    pass


# request_api_data("123")
