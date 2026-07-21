#Exercise 1
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
print(response.status_code)

#Exercise 2
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()
print(data)

#Exercise 3
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
users = response.json()
print(users[0]["name"])
print(users[0]["email"])

#User Directory Viewer
import requests
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
if response.status_code == 200:
    users = response.json()
    print("----------------------------")
    print("User Directory")
    print("----------------------------")
    for user in users:
        print("Name :", user["name"])
        print("Email:", user["email"])
        print("City :", user["address"]["city"])
        print("----------------------------")
else:
    print("Failed to fetch data!")
    print("Status Code:", response.status_code)