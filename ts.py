import requests


username = "yohanesyoshua"
password = "faisal"
password_bank = "1111"

ITEM = {
    "pd": 68,
    "grs": 71,
    "atb": 440,
    "brs": 74,
    "wrs": 75,
    "diamond": 67
}

def get_cookies():
    url = "https://seal-gladius.com/login"
    data = {
        "username": username,
        "password": password,
        "is_ajax": 1
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.cookies

    return None

def purchase(item_id):
    cookies = get_cookies()
    if not cookies:
        print("failed purchase")
        return None

    if item_id == ITEM['atb']:
        url = "https://seal-gladius.com/itemmall-bayar"
    else:
        url = "https://seal-gladius.com/itemmall-bayarr"

    data = {
        "passbank": password_bank,
        "idmall": item_id,
        "is_ajax": 1
    }

    response = requests.post(url, data=data, cookies=cookies)

    if response.status_code == 200:
        content = response.content.decode("utf-8")
        if "Success" in content:
            print("SUKSES BOR")
            return True

    return False

purchase(ITEM['diamond'])