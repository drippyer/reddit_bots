#!/bin/sh
if ! ps ax | grep "aintStupidStream.py"; then
  pipenv run python3 aintStupidStream.py
fi
