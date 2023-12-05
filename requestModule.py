import requests

# response = requests.get("https://www.google.com")
# print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"

data ={
    "title": 'Romel',
    "body": 'Hasan',
    "userId": 1,
  }
headers ={
    'Content-type': 'application/json; charset=UTF-8',
}
response = requests.post(url, json=data, headers=headers)
print(response.text)