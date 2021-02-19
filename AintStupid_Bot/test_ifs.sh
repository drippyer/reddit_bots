#!/bin/sh
if ! ps ax | grep "python3 aintStupidStream.py"; then
  pipenv run python3 aintStupidStream.py
  echo "Started"
else
  echo "Already running"
fi
