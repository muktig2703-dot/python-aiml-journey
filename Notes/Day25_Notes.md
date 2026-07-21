# Day 25 Notes - Working with APIs in Python
# Topics Covered
API (Application Programming Interface)
`requests` Library
GET Request
`response.status_code`
`response.json()`
JSON Response
User Directory Viewer Project

# 1. What is an API?
## Definition
An API (Application Programming Interface) is a set of rules that allows different software applications to communicate with each other.
Using APIs, Python programs can request data from servers and receive responses over the internet.
Examples of API usage:
Weather applications
Google Maps
Online payment systems
Social media platforms
AI models (OpenAI, Gemini)
News applications

# 2. The `requests` Library
The `requests` library is one of the most popular Python libraries for sending HTTP requests.
Installation:
bash
pip install requests
Import statement:
python
import requests
It simplifies communication with web servers.

# 3. GET Request
A GET request is used to retrieve data from a server.
Example:
python
import requests
response = requests.get("https://jsonplaceholder.typicode.com/users")
The server returns a response that contains the requested information.

# 4. `response.status_code`
The `status_code` attribute tells whether the request was successful.
Example:
python
print(response.status_code)
Common HTTP Status Codes:
| Status Code | Meaning               |
| ----------- | --------------------- |
| 200         | Request Successful    |
| 201         | Resource Created      |
| 400         | Bad Request           |
| 401         | Unauthorized          |
| 403         | Forbidden             |
| 404         | Not Found             |
| 500         | Internal Server Error |
Always check the status code before processing the response.

# 5. `response.json()`
Many APIs return data in JSON format.
The `response.json()` method converts JSON into Python objects.
Example:
python
users = response.json()
The returned data can then be accessed like normal Python dictionaries and lists.

# 6. JSON Response
A typical API response looks like this:
json
{
    "name": "Leanne Graham",
    "email": "Sincere@april.biz",
    "address": {
        "city": "Gwenborough"
    }
}
Accessing values:
python
user["name"]
user["email"]
user["address"]["city"]
Nested dictionaries are common in API responses.

# 7. User Directory Viewer Project
Today's mini project performed the following tasks:
Sent a GET request to an online API.
Checked the HTTP status code.
Converted the JSON response into Python objects.
Displayed each user's:
  Name
  Email
  City
This project demonstrated how Python communicates with external web services.

# 8. Advantages of APIs
Access real-time information
Connect applications together
Automate tasks
Retrieve data from online services
Essential for web, mobile, and AI applications
Easy to integrate with Python using the `requests` library

# 9. Keywords Learned Today
API
HTTP
Request
Response
GET
`requests`
`status_code`
`response.json()`
JSON
Endpoint