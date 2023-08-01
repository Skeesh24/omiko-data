from httpx import AsyncClient
from requests import codes
from settings import Settings
import pytest


ROUTE = Settings.URL + Settings.DELETE


@pytest.mark.anyio
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
async def test_delete(prefix, params):
    async with AsyncClient(base_url=ROUTE) as ac:
        response = await ac.delete(prefix, params=params)
    assert response.status_code == codes.NO_CONTENT
