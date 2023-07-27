from requests import codes, get
from settings import Settings


def test_repo_select():
    response = get(
        Settings.URL + Settings.GET + "/product",
        params={"limit": 1, "offset": 1, "document_id": "EaEN50idqPvCymZOJlEm"},
        json=None,
    )
    assert response.status_code == codes.ok
    assert response.json() is not None
