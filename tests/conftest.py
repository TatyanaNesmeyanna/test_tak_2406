import pytest
import json
import requests
from constants import BASE_URL

@pytest.fixture(scope='session')
def token():
    # get authentication token
    _response = requests.post(url=BASE_URL + '/api/v1/auth/login',
                              data={'login': 'testlogin123', 'password': 'testlogin123', 'grantType': 'password'})
    assert _response.status_code == 200
    decoded_response = json.loads(_response.content.decode('utf-8'))
    refresh_token = decoded_response['refresh_token']
    assert refresh_token is not None
    access_token = decoded_response['access_token']
    assert access_token is not None
    return access_token
