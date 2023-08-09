from httpx import Client, codes
import pytest

from settings import Settings


def request(url, params, json):
    ROUTE = Settings.URL + Settings.PUT

    with Client() as ac:
        return ac.put(url=ROUTE + url, params=params, json=json)


@pytest.mark.parametrize(
    "prefix, params, json",
    [
        (
            "/user",
            {"document_id": "1FbLOpGcjFdYWYil9Oow"},
            {"email": "bratok2@gmail.com", "password": "apple"},
        ),
        (
            "/product",
            {"document_id": "DuQ3dJMuBSLaCZemlgg9"},
            {
                "category": "C",
                "description": "D",
                "name": "N",
                "price": 2400,
                "short_description": "SD",
            },
        ),
        (
            "/order",
            {"document_id": "6skiPrgAKrDDtcmBfnuT"},
            {"price": 240, "products": ["apple"], "user": "bratok2@gmail.com"},
        ),
        (
            "/product_category",
            {"document_id": "8BCvXNR1ljzR95O35DB5"},
            {"name": "apple", "product_count": 24},
        ),
        (
            "/office",
            {"document_id": "OVwFEbzJNfoHRpCi7Cg3"},
            {"address": "apple", "city": "apple", "email": "apple", "phone": "apple"},
        ),
        (
            "/cabinet",
            {"document_id": "18hB8529EU0GcypXmQR4"},
            {
                "cart": ["apple"],
                "city": "apple",
                "favourites": ["apple"],
                "orders": ["apple"],
                "phone": "apple",
            },
        ),
    ],
)
def test_successful_update(prefix, params, json):
    response = request(prefix, params, json)

    assert response.status_code == codes.CREATED


@pytest.mark.parametrize(
    "prefix, params, json",
    [
        (
            "/usr",
            {"document_id": "1FbLOpGcjFdYWYil9Oow"},
            {"email": "bratok2@gmail.com", "password": "apple"},
        ),
        (
            "/DVFHBJ",
            {"document_id": ""},
            {
                "category": "",
                "description": "",
                "nae": "N",
                "price": "",
                "short_description": "SD",
            },
        ),
        (
            "/34PFIDV32",
            {"documet_id": "6skiPrgAKrDDtcmBfnuT"},
            {"prie": 240, "product": ["apple"], "user": "bratok2@gmail.com"},
        ),
        (
            "/34",
            {"document_id": ""},
            {"name": "apple", "product_count": ""},
        ),
        (
            "/ИВШАД",
            {"document_id": 12},
            {"address": "", "city": 21, "email": "", "phone": ""},
        ),
        (
            "/04зпцох)*Н№р",
            {"document_id": "[18hB8529EU0GcypXmQR4]"},
            {
                "cart": ["apple"],
                "city": 3,
                "favourites": [""],
                "orders": [],
                "phone": "",
            },
        ),
        (
            "/user",
            {"document_id": ""},
            {"emal": "bratok2@gmail.com", "password": "apple"},
        ),
        (
            "/product",
            {"document_id": ""},
            {
                "category": "",
                "description": "",
                "nae": "N",
                "price": "",
                "short_description": "SD",
            },
        ),
        (
            "/order",
            {"documet_id": "6skiPrgAKrDDtcmBfnuT"},
            {"prie": 240, "product": ["apple"], "user": "bratok2@gmail.com"},
        ),
        (
            "/product_category",
            {"document_id": ""},
            {"name": "apple", "product_count": ""},
        ),
        (
            "/office",
            {"document_id": 12},
            {"address": "", "ciy": 21, "email": "", "phone": 23},
        ),
        (
            "/cabinet",
            {"document_id": "[18hB8529EU0GcypXmQR4]"},
            {
                "cart": ["apple"],
                "city": 3,
                "favourites": [""],
                "orders": "",
                "phone": "",
            },
        ),
    ],
)
def test_unprocessable_update(prefix, params, json):
    response = request(prefix, params, json)

    assert response.status_code == codes.UNPROCESSABLE_ENTITY
