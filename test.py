import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 2000, "name": "Learn Python from scratch", "views": 100000},
        {"likes": 155, "name": "How to build a REST API", "views": 99852},
        {"likes": 50, "name": "Back end developer", "views": 5000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.get(BASE + "video/6")
print(response.json())

input()

response = requests.get(BASE + "video/2")
print(response.json())

input()

response = requests.patch(BASE + "video/2", {"likes": 200, "views": 100000})
print(response.json())

input()

response = requests.delete(BASE + "video/1")
print(response.json())

input()

response = requests.get(BASE + "video/1")
print(response.json())