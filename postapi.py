import requests

# Example for POST request with custom headers
request_headers = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

request_body = {
    "id": 50,
    "title": "Learning API Testing",
    "dueDate": "2025-09-24T07:22:03.17Z",
    "completed": False
}

response = requests.post('https://fakerestapi.azurewebsites.net/api/v1/Activities',
                         headers=request_headers, json=request_body)

print(response.status_code)
print(response.json())
print(response.headers)

assert response.status_code == 200
response_body = response.json()
assert response_body['id'] == 50
