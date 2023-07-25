import pytest
from requests import get
from requests.status_codes import codes
from settings import Settings


ROUTE = Settings.URL + Settings.GET
DEFAULT_QUERY_PARAMS = {"limit": 1, "offset": 0}
default_body_compare_param = {"field_path": "email", "op_string": "==", "value": "test"}


@pytest.mark.parametrize(
    "prefix, query_params, json",
    [
        (
            "/user",
            DEFAULT_QUERY_PARAMS,
            default_body_compare_param,
        ),
        ("/product", DEFAULT_QUERY_PARAMS, None),
        ("/order", None, None),
        ("/product_category", None, None),
        ("/office", None, None),
        ("/cabinet", None, None),
    ],
)
def test_select_all_routes(prefix: str, query_params: str, json: str):
    response = get(
        ROUTE + prefix,
        params=query_params,
        json=json,
    )
    assert response.status_code == codes.ok
    assert response.json() is not None
