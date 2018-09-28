#!/usr/bin/env bash

[ -f ./env.sh ] && . ./env.sh && export DB_CONNECTION
gunicorn server:api
