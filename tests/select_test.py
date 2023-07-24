from requests import get
from requests.status_codes import codes
from settings import Settings


def test_select_user():
    response = get(
        Settings.url + "/select/user",
        params={"limit": 2, "offset": 0},
        json={"field_path": "email", "op_string": "==", "value": "test"},
    )
    assert response.status_code == codes.ok
    assert response.json() is not None
    assert len(response.json()) >= 1
