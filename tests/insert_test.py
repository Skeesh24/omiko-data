from requests import post
from requests.status_codes import codes
from settings import Settings


def test_select_query():
    response = post(
        Settings.url + "/insert/user",
        json={
            "email": "bratok2@gmail.com",
            "password": "AESRGEFfnpsiyhPYBEFncwpnsSUkm",
        },
    )
    assert response.status_code == codes.created
