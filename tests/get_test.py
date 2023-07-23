from requests import get, post


def test_select_query():
    response = post(
        "http://localhost:8000/get/user",
        params={"limit": 2, "offset": 0},
        json={"field_path": "email", "op_string": "==", "value": "test"},
    )
    assert response.status_code == 200
    assert response.json() is not None
