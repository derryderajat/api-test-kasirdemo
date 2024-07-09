import requests
import pytest
import re


def test_login():
    url = "https://kasir-api.belajarqa.com/authentications"
    payload  = {
        "email":"apapunnamanyaitu@gmail.com",
        "password":"123456"
        }
    response = requests.post(url, data=payload)
    response_data = response.json()
    
    # assert status code is 201
    assert response.status_code == 201
    # assert the status in the response is success
    assert response_data.get('status') == 'success'
    # assert message
    assert response_data.get('message') == 'Authentication berhasil ditambahkan'
    # assert value accessToken and refreshtoken is a string
    assert isinstance(response_data['data']['accessToken'], str), "acess token is not string"
    assert isinstance(response_data['data']['refreshToken'], str), "refresh token is not string"


