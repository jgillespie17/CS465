#!/usr/bin/env bash
export FLASK_APP=app.py
export FLASK_ENV=development
export APP_SETTINGS=$(pwd)/example.settings
export DB=activity_log
export DB_HOST=0.0.0.0
export SLEEP_TIME=2
flask run --host=0.0.0.0 --port $@
