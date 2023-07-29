from httpx import AsyncClient
from requests import codes
from settings import Settings
import pytest


ROUTE = Settings.URL + Settings.DELETE


@pytest.mark.anyio
@pytest.mark.parametrize(
    "prefix, params",
    [
        # ("/user", None),
        (
            "/product",
            {"document_id": "pa9xFlcIXcyDvCA5onWE"},
        ),
        # (
        #     "/order",
        #     None,
        # ),
        # (
        #     "/product_category",
        #     {"document_id": "U0Kg4CtDyNRTnLpfa08V"},
        # ),
        # (
        #     "/office",
        #     {},
        # ),
        # ("/cabinet", None),
    ],
)
async def test_delete(prefix, params):
    async with AsyncClient(base_url=ROUTE) as ac:
        response = await ac.delete(prefix, params=params)
    assert response.status_code == codes.NO_CONTENT
