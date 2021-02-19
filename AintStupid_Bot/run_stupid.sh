#!/bin/sh
if ! ps ax | grep "[a]intStupidStream.py"; then
  echo "Starting"
  pipenv run python3 aintStupidStream.py
else
  echo "Already running"
fi
