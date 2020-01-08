from flask import Flask, jsonify, abort
VOTES = [
            {
                        'post_id': 0,
                                'vote_count': -1,
                                    },
                {
                            'post_id': 1,
                                    'vote_count': 5,
                                        },
                    {
                                'post_id': 2,
                                        'vote_count': 42,
                                            },
                    ]
app = Flask(__name__)

@app.route('/api/votes')
def votes():
    return jsonify(VOTES)

@app.route('/api/votes/<int:id>', methods=["GET"])
def single_post(id):
    if id < 0 or id >= len(VOTES):
        abort(404)
    return jsonify(VOTES[id])
