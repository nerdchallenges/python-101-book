# Example 1 - Sending your First GET Request
import requests

# response = requests.get('https://swapi.dev/api/people/1/')
# print(f"Status Code = {response.status_code}")
# print(f"Response from Website = {response.text}")


# data = response.json()
# print(type(data))
# print(data['name'])
# print(data['height'])
# print(data['birth_year'])
# print(data['gender'])

# data = {'name': 'John Smith'}
# response = requests.post('https://swapi.dev/api/people/', data)
# print(response.status_code)
# print(response.text)

# data = {'name': 'John Smith'}
# response = requests.delete('https://swapi.dev/api/people/1/')
# print(response.status_code)
# print(response.text)

# Example 2 - Sending a Post Request? Oh no.
# data = {'name': 'John Smith'}
# response = requests.post('https://swapi.dev/api/people/1', data)
# print(response.status_code)
# print(response.text)

# # Example 3 - Finding a better API :) Sending a GET request again
# # https://jsonplaceholder.typicode.com/posts
# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# print(f"Status Code = {response.status_code}")
# print(f"Response from Website = {response.text}")

# # Example 4 - Sending a POST again
data = {
  "title": "Python Requests Library is awesome!",
  "body": "Pretty cool yea? :D"
}
response = requests.post('https://jsonplaceholder.typicode.com/posts/', data)
print(response.status_code)
print(response.text)

# # Example 5 - Sending a DELETE Request
response = requests.delete('https://jsonplaceholder.typicode.com/posts/101')
print(response.status_code)
print(response.text)