import requests

# Example for PUT request with custom headers and Id in the path
request_headers = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json'
}

request_body = {
    "id": 50,
    "title": "Learning Updated using Put API Testing",
    "dueDate": "2025-09-24T07:22:03.17Z",
    "completed": True
}

response = requests.put('https://fakerestapi.azurewebsites.net/api/v1/Activities/50',
                        headers=request_headers, json=request_body)

print(response.status_code)
print(response.json())
print(response.headers)

assert response.status_code == 200
response_body = response.json()
assert response_body['id'] == 50
