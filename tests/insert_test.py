from requests import post


def test_select_query():
    response = post(
        "http://localhost:8000/insert/user",
        json={"email": "bratok@gmail.com", "password": "AESRGEFfnpsiyhPYBEFncwpnsSUkm"},
    )
    assert response.status_code == 201
    assert response.json() is not None
    assert len(response.json()) >= 1
