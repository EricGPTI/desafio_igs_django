from requests import get

url = "http://127.0.0.1:8000/"

def test_endpoint_employees_status_code_200():
    resp = get(url + "employees/")
    assert resp.status_code == 200


# def test_employee_id_1():
#     resp = get(url + "employees/")
#     assert resp.status_code == 200