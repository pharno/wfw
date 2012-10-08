#!/bin/sh
while true; do
  python server.py &
  PID=$!
  sleep 1
  inotifywait -r "." -e modify
  kill $PID
done