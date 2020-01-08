#!/bin/bash
export WOLFIT_SETTINGS=$(pwd)/dev.settings
export POST_URL='http://0.0.0.0:5001/api/activities'
flask run --host=0.0.0.0
