import requests
import pytest
import re

def test_register():
    url = "https://kasir-api.belajarqa.com/registration"
    payload  = {
        "name":"dd-test-toko-1",
        "email":"apapunnamanyaitugmail.com",
        "password":"123456"
        }
    response = requests.post(url, data=payload)
    response_data = response.json()
    
    # assert status code is 201
    assert response.status_code == 201
    # assert the status in the response is success
    assert response_data.get('status') == 'success'
    # assert value name is a string
    assert isinstance(response_data['data']['name'], str), "Email format is invalid"
    # Assert the 'email' has a valid email format
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    assert re.match(email_pattern, response_data['data']['email']), "Email format is invalid"




if __name__ == "__main__":
    test_register()