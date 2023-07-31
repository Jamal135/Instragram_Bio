#!/bin/bash

# Wait for Selenium to be ready
for i in {1..10}; do
  if curl -s "http://selenium:4444/wd/hub/status" | grep -q "ready"; then
    echo "Selenium is ready!"
    # Run the Python script
    python3 -u instagram.py production
    exit 0
  fi
  echo "Waiting for Selenium..."
  sleep 5
done
echo "Selenium is not ready, exiting..."
exit 1



