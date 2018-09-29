#!/usr/bin/env bash

[ -f ./config ] && . ./config && export DB_CONNECTION
gunicorn server:api
