from httpx import Client
from requests import post
from requests.status_codes import codes
from settings import Settings
import pytest


ROUTE = Settings.URL + Settings.POST


@pytest.mark.parametrize(
    "prefix, dictionary",
    [
        (
            "/user",
            {
                "email": "bratok2@gmail.com",
                "password": "AESRGEFfnpsiyhPYBEFncwpnsSUkm",
            },
        ),
        (
            "/product",
            {
                "name": "test",
                "description": "test",
                "short_description": "test",
                "price": 24,
                "category": "test",
            },
        ),
        (
            "/order",
            {
                "user": "bratok2@gmail.com",
                "products": ["test"],
                "price": 24,
            },
        ),
        ("/product_category", {"name": "test", "product_count": 24}),
        (
            "/office",
            {
                "city": "test",
                "address": "test",
                "phone": "test",
                "email": "test",
            },
        ),
        (
            "/cabinet",
            {
                "cart": ["test"],
                "favourites": ["test"],
                "orders": ["test"],
                "city": "test",
                "phone": "test",
            },
        ),
    ],
)
def test_insert_in_models(prefix, dictionary):
    with Client() as ac:
        response = ac.post(url=ROUTE + prefix, json=dictionary)
    assert response.status_code == codes.created
    assert response.json() is not None
    assert len(response.json()) >= 1
