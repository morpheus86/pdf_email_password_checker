import requests
import hashlib
import sys


# request data and get response
def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the Api and Try again")
    return res


# read response
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in
              hashes.text.splitlines())  # splitting the hash and the count into its own tuple
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


# check password if it exists in API response
def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode(
        "utf-8")).hexdigest().upper()  # password.encode("utf-8").hexdigest().upper() is necessary to encode unicode
    # before hashing it
    first5_char, rest = sha1_password[:5], sha1_password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, rest)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times ... You should probably use a different password")
        else:
            print(f"{password} was NOT FOUND. Carry On!")


main(sys.argv[1:])

