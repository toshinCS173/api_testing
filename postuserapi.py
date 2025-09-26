import requests

# Exercise1 Part 1
# Example for POST request with custom headers
request_headers = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 0b5b0eac4854cb5fdd8048c8406cb60fc8476e30dee6d2fb8a64a7ad7e86749e'
}

request_body = {
    "name": "Rep. Tejas Kaniyar2323",
    "email": "wqqwerodljerejl34@legros.example",
    "gender": "male",
    "status": "inactive"
}

response = requests.post('https://gorest.co.in/public/v2/users',
                         headers=request_headers, json=request_body)

print(response.status_code)
print(response.json())
print(response.headers)

assert response.status_code == 201
response_body = response.json()
print(response_body['id'])

id = response_body['id']
url = "https://gorest.co.in/public/v2/users/"+str(id)

# Exercise1 Part 2
print(url)
get_response = requests.get(url, headers=request_headers)

print(get_response.status_code)
print(get_response.json())

assert get_response.status_code == 200
# assert get_response.json()['id'] == response_body['id']
