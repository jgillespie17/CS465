#!/usr/bin/env bash

coverage run --omit "tests/test_app.py","activity_logger.py" --source "." -m py.test
coverage html
open htmlcov/index.html
