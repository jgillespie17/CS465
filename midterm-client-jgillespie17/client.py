from flask import Flask, jsonify, abort, request
from datetime import datetime
app = Flask(__name__)

cool = [
        {
            'even': 'false',
            'inverse': 2,
            }
        ];
@app.route('/api/intdata/<int:id>', methods=["GET"])
def single_activity(id):
    new_dict = {
            "even": "false",
            "inverse": id,
            }
    if id % 2 == 0:
        new_dict["even"] = "true"
    new_num = 0 - id
    new_dict["inverse"] = new_num
    return new_dict
