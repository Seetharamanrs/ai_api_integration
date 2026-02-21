import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "My First API Post",
    "body": "Learning API with Python",
    "userId": 1
}

response = requests.post(url, json=data)

response_data = response.json()

print("New Post ID:", response_data["id"])
print("Title:", response_data["title"])
print("Message:", response_data["body"])