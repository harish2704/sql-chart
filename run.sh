#!/usr/bin/env bash

[ -f ./config ] && . ./config && export DB_CONNECTION
bindAddress=${BIND_ADDRESS:-'127.0.0.1:8000'}
gunicorn server:api -b $bindAddress "$@"
