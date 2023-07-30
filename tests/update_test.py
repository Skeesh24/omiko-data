from httpx import AsyncClient
import pytest

from settings import Settings


@pytest.mark.anyio
@pytest.mark.parametrize(
    "prefix, params, json",
    [
        ("/product", {}, {}),
        ("/order", {}, {}),
        ("product_category", {}, {}),
        ("order_category", {}, {}),
    ],
)
async def test_update_all_routes(prefix, params, json):
    async with AsyncClient() as ac:
        response = await ac.put(
            url=Settings.URL + Settings.PUT + prefix, params=params, json=json
        )

    assert response.status_code == 201
