import json
import requests
import time

url = "http://0.0.0.0:8080/api/post"

while True:
    r = requests.get(url)
    data = json.loads(r.text)
    print("version: " + data[3])
    print("Title of first post: " + data[0]["title"])
    time.sleep(2)
