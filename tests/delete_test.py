from httpx import Client
from requests import codes
from settings import Settings
import pytest


ROUTE = Settings.URL + Settings.DELETE


@pytest.mark.parametrize(
    "prefix, params",
    [
        ("/user", {"document_id": "267U3f0pKDfnKWx4N0tq"}),
        (
            "/product",
            {"document_id": "pa9xFlcIXcyDvCA5onWE"},
        ),
        (
            "/order",
            {"document_id": "BI6xTsN60lxZUcrW5FA9"},
        ),
        (
            "/product_category",
            {"document_id": "U0Kg4CtDyNRTnLpfa08V"},
        ),
        (
            "/office",
            {"document_id": "U0Kg4CtDyNRTnLpfa08V"},
        ),
        ("/cabinet", {"document_id": "HUQD0azry2g7e7WpHIrV"}),
    ],
)
def test_delete(prefix, params):
    with Client(base_url=ROUTE) as c:
        response = c.delete(prefix, params=params)
    assert response.status_code == codes.NO_CONTENT
