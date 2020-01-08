import requests
import json

url = "https://reqres.in/api/unknown"

def get_colors(url)
    r = requests.get(url)
    colors = json.loads(r.text)
    if isinstance(colors, dict):
        if(colors['id'] == 0:
            print colors['name']
        if(colors['id'] == 1:
            print colors['name']
