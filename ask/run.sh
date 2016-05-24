#!/usr/bin/env bash
sudo gunicorn --bind 0.0.0.0:8000 --access-logfile acc.log --error-logfile err.log ask.wsgi:application