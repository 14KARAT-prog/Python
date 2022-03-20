import requests

URL_GET = 'https://jsonplaceholder.typicode.com'
URL_POST = 'https://reqres.in'


response = requests.get(f"{URL_GET}/users/1")
responseCopy = response.json().copy()
responseCopy.pop('id')


post = requests.post(f"{URL_POST}/api/users", json=responseCopy)

print(post.json())
