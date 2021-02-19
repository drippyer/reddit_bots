#!/bin/sh
if ! ps ax | grep "[a]intStupidStream.py"; then
  pipenv run python3 aintStupidStream.py
  echo "Started"
else
  echo "Already running"
fi
