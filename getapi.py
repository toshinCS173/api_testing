import requests

#GET All Activities
response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities')

print(response.status_code)
print(response.json())
print(response.headers)

assert response.status_code == 200

#Get Activities by Id API

request_headers ={
    'Accept': 'text/plain'
}

response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities/25', headers=request_headers)

print(response.status_code)
print(response.json())
print(response.headers)

assert response.status_code == 200