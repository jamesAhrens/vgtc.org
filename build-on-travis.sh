#!/bin/sh
. ./venv/bin/activate
git checkout master
make $1
