#!/bin/bash

LOG_FILE="/var/log/check_disk.log"
DISK_IDS_FILE="/etc/disk_ids.txt"

if [ ! -f "$LOG_FILE" ]; then
    touch "$LOG_FILE"
    chmod 664 "$LOG_FILE"
fi

if [ ! -f "$DISK_IDS_FILE" ]; then
    touch "$DISK_IDS_FILE"
    chmod 664 "$DISK_IDS_FILE"
fi

for DISK in /dev/sd*; do
    if [[ -b "$DISK" ]]; then
        DISK_UUID=$(blkid -s UUID -o value "$DISK")
        if grep -q "$DISK_UUID" "$DISK_IDS_FILE"; then
            FILESYSTEM=$(lsblk -no FSTYPE "$DISK")
            echo "$(date): Disk $DISK_UUID founded. File system: $FILESYSTEM" >> "$LOG_FILE"
            if [ "$FILESYSTEM" != "btrfs" ]; then
                echo "$(date): Disk formatting $DISK_UUID in btrfs." >> "$LOG_FILE"
                mkfs.btrfs "$DISK"
            else
                echo "$(date): Disk $DISK_UUID formatted in btrfs." >> "$LOG_FILE"
            fi
        else
            echo "$(date): Disk $DISK_UUID not found, formatting in btrfs." >> "$LOG_FILE"
            mkfs.btrfs "$DISK"
            echo "$DISK_UUID" >> "$DISK_IDS_FILE"
            echo "$(date): UUID $DISK_UUID saved." >> "$LOG_FILE"
        fi
    fi
done