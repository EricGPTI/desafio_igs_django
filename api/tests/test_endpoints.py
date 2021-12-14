import requests
import json

url = "http://127.0.0.1:8000/api/v1/"
headers = {'Content-Type': 'application/json', 'Authorization': 'Token 5f04f3ed15bc62419520c149ca1543620d88ce64'}
endpoint = "employees/"


def test_endpoint_employees_get_status_code_200():
    resp = requests.get(f"{url}{endpoint}", headers=headers)
    assert resp.status_code == 200


def test_endpoint_employees_post_status_code_201():
    body = {
        "name": "Eric Gomes",
	    "email": "ericgpti@gmail.com",
	    "department": "TI"
    }
    resp = requests.post(f"{url}{endpoint}", headers=headers, data=json.dumps(body))
    assert resp.status_code == 201

def test_endpoint_employees_delete_status_code_200():
    id = requests.get(f"{url}{endpoint}", headers=headers).json()[0]['id']
    resp = requests.delete(f"{url}{endpoint}{id}", headers=headers)
    assert resp.status_code == 200