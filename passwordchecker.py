#!/bin/python3

import requests
import hashlib
import sys
import termcolor


def open_file(filename):
    try:
        with open(filename, "r") as f:
            text = f.readlines()
        return text
    except FileNotFoundError:
        termcolor.cprint(f"File could not be found.", "red")


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


def main(file):
    for password in open_file(file):
        password = password.strip()
        count = check_password(password)
        if count:
            termcolor.cprint(f'[-] "{password}" was found {count} times.', "red")
        else:
            termcolor.cprint(f'[+] "{password}" was NOT found.', "green")


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv[1]))
    except:
        pass
