import requests
import hashlib
import sys


def request_api_data(query_chars):
    url = f"https://api.pwnedpasswords.com/range/{query_chars}"
    response = requests.get(url)
    status = response.status_code
    if status != 200:
        raise RuntimeError(f"Error fetching: {status}")
    return response


def get_password_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    return 0


def check_password(password):
    sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_5_chars, remaining_chars = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first_5_chars)
    return get_password_count(response, remaining_chars)


def main(args):
    for password in args:
        count = check_password(password)
        if count:
            print(f'"{password}" was found {count} times.')
        else:
            print(f'"{password}" was NOT found.')
