from httpx import Client, codes
from settings import Settings
import pytest


def request(url, params):
    ROUTE = Settings.URL + Settings.DELETE

    with Client(base_url=ROUTE) as c:
        response = c.delete(url=url, params=params)
    return response


@pytest.mark.parametrize(
    "prefix, params",
    [
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
def test_successful_delete(prefix, params):
    assert request(prefix, params).status_code == codes.NO_CONTENT


@pytest.mark.parametrize(
    "prefix, params",
    [
        ("/product", {"document_id": ""}),
        (
            "/order",
            {"document_id": ""},
        ),
        (
            "/product_category",
            {"document_id": ""},
        ),
        (
            "/office",
            {"document_id": ""},
        ),
        ("/cabinet", {"document_id": ""}),
    ],
)
def test_badrequest_delete(prefix, params):
    assert request(prefix, params).status_code == codes.BAD_REQUEST


@pytest.mark.parametrize(
    "prefix, params",
    [
        ("/use", {"document_id": "267U3f0pKDfnKWx4N0tq"}),
        (
            "/prouct",
            {"document_id": "pa9xFlcIXcyDvCA5onWE"},
        ),
        (
            "/orer",
            {"document_id": "BI6xTsN60lxZUcrW5FA9"},
        ),
        (
            "/виаиваи",
            {"document_id": "U0Kg4CtDyNRTnLpfa08V"},
        ),
        (
            "/342",
            {"document_id": "U0Kg4CtDyNRTnLpfa08V"},
        ),
        ("/34ацуывПШГЛ", {"document_id": "HUQD0azry2g7e7WpHIrV"}),
    ],
)
def test_unprocessable_delete(prefix, params):
    assert request(prefix, params).status_code == codes.UNPROCESSABLE_ENTITY
