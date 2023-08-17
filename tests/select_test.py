from httpx import Client, codes
import pytest
from settings import Settings


DEFAULT_QUERY_PARAMS: dict = {"limit": 1, "offset": 0}
DEFAULT_BODY_COMPARE_PARAMS: dict = {
    "field_path": "email",
    "op_string": "==",
    "value": "test",
}


def request(url, params, json):
    ROUTE = Settings.URL + Settings.GET

    with Client() as ac:
        return ac.post(
            ROUTE + url,
            params=params,
            json=json,
        )


@pytest.mark.parametrize(
    "prefix, query_params, json",
    [
        ("/product", DEFAULT_QUERY_PARAMS, None),
        ("/order", None, None),
        ("/product_category", None, None),
        ("/office", None, None),
        ("/cabinet", None, None),
    ],
)
def test_successful_select(prefix: str, query_params: str, json: str):
    response = request(prefix, query_params, json)

    assert response.status_code == codes.ok
    assert response.json() is not None


@pytest.mark.parametrize(
    "prefix, query_params, json",
    [
        (
            "/product",
            {},
            {
                "field_pth": "email",
                "op_string": "",
                "ve": "tet",
            },
        ),
        (
            "/order",
            {
                "field_path": "email",
                "op_string": "==",
                "value": "test",
            },
            {},
        ),
        ("/product_category", {}, {"": ""}),
        ("/office", "", {}),
        ("/cabinet", {}, ""),
        (
            "/uer",
            DEFAULT_QUERY_PARAMS,
            {},
        ),
        ("/prodsduct", DEFAULT_QUERY_PARAMS, None),
        ("/ц8рщуашы", {}, None),
        ("/79YOIWFE", None, None),
        ("/438ЩРАУЦШ", None, {}),
        ("/Ы", {}, {}),
    ],
)
def test_unprocessable_select(prefix: str, query_params: str, json: str):
    response = request(prefix, query_params, json)

    assert response.status_code == codes.UNPROCESSABLE_ENTITY
