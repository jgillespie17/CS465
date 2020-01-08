#!/usr/bin/env bash

export WOLFIT_SETTINGS=$(pwd)/test.settings
export FLASK_ENV=test
export FLASK_DEBUG=0
coverage run --source "." --omit load_reddit_posts.py -m py.test
coverage html
open htmlcov/index.html
