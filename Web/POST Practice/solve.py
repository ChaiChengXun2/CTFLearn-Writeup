import requests

url = "http://165.227.106.113/post.php"

data = {
    "username": "admin",
    "password": "71urlkufpsdnlkadsf"
}

r = requests.post(url, data=data)
print(r.text)