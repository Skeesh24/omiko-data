from requests import delete
from requests.status_codes import codes
from settings import Settings
import pytest


ROUTE = Settings.URL + Settings.DELETE


@pytest.mark.parametrize(
    "prefix, params, data",
    [
        ("/user", None, None),
        (
            "/product",
            None,
            {"field_path": "name", "op_string": "==", "value": "test"},
        ),
        (
            "/order",
            None,
            {
                "user": "bratok2@gmail.com",
                "products": ["test"],
                "price": 24,
            },
        ),
        (
            "/product_category",
            {"document_id": "U0Kg4CtDyNRTnLpfa08V"},
            {"name": "test", "product_count": 24},
        ),
        (
            "/office",
            {},
            {"city": "test", "address": "test", "phone": "test", "email": "test"},
        ),
        ("/cabinet", None, None),
    ],
)
def test_delete(prefix, params, data):
    response = delete(ROUTE + prefix, params=params, json=data)
    assert response.status_code == codes.NO_CONTENT
