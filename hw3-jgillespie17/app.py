from flask import Flask, jsonify, abort, request
from mongoengine import *
import time
from datetime import datetime
from activity_logger import *
import os
app = Flask(__name__)

host = os.environ.get('DB_HOST')
db = os.environ.get('DB')
connect(host=host)


URL = 'https://0.0.0.0:5001'
sleep_time = os.getenv('SLEEP_TIME', default=0)


class ActivityLog(Document):
     user_id = IntField(required=True)
     username = StringField(required=True, max_length=64)
     timestamp = DateTimeField(default=datetime.utcnow)
     details = StringField(required=True)


#activities = ActivityLog.objects.all().order_by("-timestamp").limit(10)


@app.route('/api/activities/', methods=["GET"])
def recent_activities():
    numLogs = 10
    activity_log = []
    activity = ActivityLog.objects.all().order_by("-timestamp").limit(numLogs)
    print(activity)
    for log in activity:
        activity_log.append(
                {
                    'user_id' : log.user_id,
                    'username' : log.username,
                    'timestamp' : log.timestamp,
                    'details' : log.details
                    })
    return jsonify(activity_log)

@app.route('/api/activities/<int:id>', methods=["GET"])
def single_activity(id):
    if id < 0 or id >= len(activity_log):
        abort(404)
    return jsonify(activity_log[id])

@app.route('/api/activities', methods=["POST"])
def add_activity():
    if not request.json:
        abort(400)
    new_activity = request.get_json()
    if 'user_id' not in new_activity or 'username' not in new_activity or 'details' not in new_activity:
        abort(400)
    b = ActivityLog(
            user_id=new_activity['user_id'],
            username=new_activity['username'],
            timestamp=str(datetime.utcnow()),
            details=new_activity['details']
            )
    b.save() 
    time.sleep(int(sleep_time))
    new_activity['id'] = str(b.id)
    new_activity['location'] = "/api/activites/" + str(b.id)
    
    return jsonify(new_activity)

