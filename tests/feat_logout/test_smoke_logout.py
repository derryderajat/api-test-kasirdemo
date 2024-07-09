# https://kasir-api.belajarqa.com/authentications
import requests
import pytest

@pytest.fixture
def test_login():
    url = "https://kasir-api.belajarqa.com/authentications"
    payload  = {
        "email":"apapunnamanyaitu@gmail.com",
        "password":"123456"
    }
    response = requests.post(url, data=payload)
    response_data = response.json()
    return response_data['data']['refreshToken']

def test_logout(test_login):
    url = "https://kasir-api.belajarqa.com/authentications"
    refreshToken = test_login
    payload  = {
        "refreshToken": refreshToken
    }
    response = requests.delete(url, data=payload)
    response_data= response.json()
    assert response.status_code==200
    # {"status":"success","message":"Refresh token berhasil dihapus"}
    assert response_data['message'] == 'Refresh token berhasil dihapus'

