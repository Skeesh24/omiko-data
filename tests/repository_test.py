from requests import codes, get
from settings import Settings
import pytest


@pytest.mark.parametrize(
    "params, json",
    [
        (
            {
                "limit": 1,
                "offset": 0,
            },
            {"field_path": "name", "op_string": "==", "value": "test"},
        ),
        ({"limit": 1, "offset": 2}, None),
        (
            {"limit": 0, "offset": 0},
            {"field_path": "name", "op_string": "==", "value": "test"},
        ),
    ],
)
def test_repo_select(params, json):
    response = get(
        Settings.URL + Settings.GET + "/product",
        params=params,
        json=json,
    )
    assert response.status_code == codes.ok
    assert response.json() is not None
