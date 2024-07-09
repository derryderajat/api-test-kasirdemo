import requests
import pytest
import re

@pytest.mark.parametrize(
    'payload, expected_status_code, expected_status, expected_name, expected_email_pattern',
    [
        (
            {
                "name": "dd-test-toko-1",
                "email": "apapunnamanyaitu@gmail.com",
                "password": "123456"
            },
            201, 'success', str, r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        ),
        (
            {
                "name": "dd-test-toko-2",
                "email": "invalid-email",
                "password": "123456"
            },
            400, 'fail', str, None 
        ),
        (            
            {
                "name": "dd-test-toko-3",
                "email": "apapunnamanyaitu@gmail.com",
                "password": "123456"
            },
            400, 'duplicate email', str, r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        ),
        (
            {
                "name": None,
                "email": "apapunnamanyaitu1@gmail.com",
                "password": "123456"
            },
            400, 'fail', str, r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            # name cannot be null
        ),
        (
            {
                "name": "dd-test-toko-5",
                "email": "apapunnamanyaitu5@gmail.com",
                "password": ""
            },
            400, 'fail', str, r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            # password cannot be empty string
        ),
        (
            {
                "name": "dd-test-toko-6",
                "email": "apapunnamanyaitu6@gmail.com",
                "password": None
            },
            400, 'fail', str, r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
            # password cannot be null
        ),


    ], ids=[
        "valid input",
        "Invalid email",
        "Duplicate email",
        "Name is null",
        "Password empty",
        "Password is null"
    ]
)
def test_register(payload, expected_status_code, expected_status, expected_name, expected_email_pattern):
    url = "https://kasir-api.belajarqa.com/registration"
    response = requests.post(url, json=payload)
    response_data = response.json()
    
    # Assert the status code
    assert response.status_code == expected_status_code
    
    # Assert the status in the response
    assert response_data.get('status') == expected_status

    # assert response time is under 500ms
    response_time_ms = response.elapsed.total_seconds() * 1000
    assert response_time_ms < 500, f"Response time {response_time_ms} ms exceeds 500 ms"

    
    # Assert the name is a string if expected_status is 'success'
    if expected_status == 'success':
        assert isinstance(response_data['data']['name'], expected_name), "Name is not a string"
    
    # Assert the email format if expected_status is 'success'
    if expected_status == 'success' and expected_email_pattern:
        assert re.match(expected_email_pattern, response_data['data']['email']), "Email format is invalid"

if __name__ == "__main__":
    test_register()
