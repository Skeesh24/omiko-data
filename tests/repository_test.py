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
        ({"limit": 1, "offset": 1}, None),
        (
            {"limit": 0, "offset": 0},
            {"field_path": "name", "op_string": "==", "value": "test"},
        ),
        ({"limit": 100, "offset": 0}, None),
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
    assert len(response.json()) > 0 or response.json() == []
