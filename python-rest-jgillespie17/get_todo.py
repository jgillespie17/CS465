import json
import requests
import sys

get_url = "https://jsonplaceholder.typicode.com/todos/"
url = get_url + sys.argv[1]
r = requests.get(url)
if r.status_code == 200:
    data = json.loads(r.text)
    print(data)
