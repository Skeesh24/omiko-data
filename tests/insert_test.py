from httpx import Client, codes
from settings import Settings
import pytest


def request(url, content):
    ROUTE = Settings.URL + Settings.POST

    with Client() as ac:
        return ac.post(url=ROUTE + url, json=content)


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
def test_successful_insert(prefix, dictionary):
    response = request(prefix, dictionary)
    assert response.status_code == codes.CREATED
    assert response.json() is not None
    assert len(response.json()) >= 1


@pytest.mark.parametrize(
    "prefix, dictionary",
    [
        (
            "/user",
            {
                "email": [],
                "password": "AESRGEFfnpsiyhPYBEFncwpnsSUkm",
            },
        ),
        (
            "/product",
            {
                "ame": "",
                "escription": "",
                "hort_description": "",
                "pric": 0,
                "ategory": "",
            },
        ),
        (
            "/order",
            {
                "": "bratok2@gmail.com",
                "": ["test"],
                "": 24,
            },
        ),
        ("/product_category", {"name": "", "product_count": ""}),
        (
            "/office",
            {
                "city": "",
                "": "test",
                "phone": "",
                "": "test",
            },
        ),
        (
            "/cabinet",
            {
                "cart": [""],
                "favourites": "",
                "orders": ["test"],
                "city": "",
                "phone": "[]",
            },
        ),
        (
            "/usr",
            {},
        ),
        (
            "/rth54нукп",
            {},
        ),
        (
            "/4453",
            {},
        ),
        ("/produccategory", {"name": "", "product_count": ""}),
        (
            "/4еупкви",
            {},
        ),
        (
            "/348OHS",
            {
                "phone": "[]",
            },
        ),
    ],
)
def test_unprocessable1_insert(prefix, dictionary):
    response = request(prefix, dictionary)
    assert response.status_code == codes.UNPROCESSABLE_ENTITY
