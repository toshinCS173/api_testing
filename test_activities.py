import pytest
import requests


def test_getrequest():
    request_headers = {
        'Accept': 'text/plain'
    }

    response = requests.get(
        'https://fakerestapi.azurewebsites.net/api/v1/Activities/5', headers=request_headers)

    assert response.status_code == 200
