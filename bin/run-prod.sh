#!/usr/bin/env bash


/usr/local/bin/uwsgi --uid deploy --gid deploy --master --processes 4 --socket 0.0.0.0:5000 --protocol=http -w app:app
