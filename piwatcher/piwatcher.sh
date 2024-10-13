#!/bin/bash

LOG_FILE="/home/piwatcher/piwatcher_status.log"
if [ ! -e "$LOG_FILE" ]; then
    touch "$LOG_FILE"
fi

echo "$(date '+%Y-%m-%d %H:%M:%S'): $(/usr/local/bin/piwatcher status)" >> "$LOG_FILE"


defaults=$(/usr/local/bin/piwatcher defaults)

if echo "$defaults" | grep -q "disabled"; then
    /usr/local/bin/piwatcher defaults 180 30
    sleep 1
    echo "Defaults set to: $(/usr/local/bin/piwatcher defaults)"
fi

while true; do
    status=$(/usr/local/bin/piwatcher status)
    if echo "$status" | grep -q "button_pressed"; then
        echo "Shutting down..."
        /usr/local/bin/piwatcher watch 30
        sudo shutdown -h now
        break
    fi
    sleep 1
done