from httpx import AsyncClient
import pytest

from settings import Settings


@pytest.mark.anyio
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
async def test_update_all_routes(prefix, params, json):
    async with AsyncClient() as ac:
        response = await ac.put(
            url=Settings.URL + Settings.PUT + prefix, params=params, json=json
        )

    assert response.status_code == 201
