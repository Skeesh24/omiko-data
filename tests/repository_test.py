from httpx import AsyncClient
from requests import codes, get
from settings import Settings
import pytest


@pytest.mark.anyio
@pytest.mark.parametrize(
    "prefix, params, json",
    [
        (
            "/product",
            {
                "limit": 1,
                "offset": 0,
            },
            {"field_path": "name", "op_string": "==", "value": "test"},
        ),
        ("/product", {"limit": 1, "offset": 1}, None),
        (
            "/product",
            {"limit": 0, "offset": 0},
            {"field_path": "name", "op_string": "==", "value": "test"},
        ),
        ("/user", {"limit": 100, "offset": 0}, None),
        (
            "/user",
            {
                "limit": 1,
                "offset": 0,
            },
            {"field_path": "name", "op_string": "==", "value": "test"},
        ),
        ("/user", {"limit": 1, "offset": 1}, None),
        (
            "/user",
            {"limit": 0, "offset": 0},
            {"field_path": "name", "op_string": "==", "value": "test"},
        ),
        ("/order", {"limit": 100, "offset": 0}, None),
        (
            "/order",
            {
                "limit": 1,
                "offset": 0,
            },
            {"field_path": "name", "op_string": "==", "value": "test"},
        ),
        ("/order", {"limit": 1, "offset": 1}, None),
        (
            "/order",
            {"limit": 0, "offset": 0},
            {"field_path": "name", "op_string": "==", "value": "test"},
        ),
        ("/order", {"limit": 100, "offset": 0}, None),
    ],
)
async def test_repo_select(prefix, params, json):
    async with AsyncClient() as ac:
        response = await ac.post(
            url=Settings.URL + Settings.GET + prefix,
            params=params,
            json=json,
        )
    assert response.status_code == codes.ok
    assert response.json() is not None
    assert len(response.json()) > 0 or response.json() == []
