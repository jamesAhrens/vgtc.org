#!/bin/sh
. ./venv/bin/activate
git checkout production
make $1
