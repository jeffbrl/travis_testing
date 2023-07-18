#!/usr/bin/env bash

python3 run.py > /dev/null &
nosetests --with-coverage
