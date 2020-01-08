import pytest
from flask import jsonify, request
import requests
from datetime import datetime
from app import add_activity, recent_activities

recent_url = "http://0.0.0.0:5001/api/activities/"
post_url = "http://0.0.0.0:5001/api/activities"
def test_add_activity():
    activity = {
            "user_id" : 201,
            "username" : "George", 
            "details" : "paul is alive",
            }
    r = requests.post(post_url, json=activity)
    assert r.status_code == 201 or 200

def test_add_activity_empty_user():
    activity = {}
    r = requests.post(post_url, json=activity)
    assert r.status_code == 400

def test_add_activity_no_user_id():
    activity = {
            "username" : "George",
            "details" : "testing"
            }
    r = requests.post(post_url, json=activity)
    assert r.status_code == 400

def test_recent_activities():
    r = requests.get(recent_url)
    assert r.status_code == 200
