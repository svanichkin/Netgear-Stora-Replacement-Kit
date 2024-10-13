# Disk auto format

The logic of this script is simple: we save logs in /var/log/check_disk.log and store the IDs of disks that have already been inserted into the device in /etc/disk_ids.txt. If the disk is not formatted, it gets formatted.

```
sudo apt install btrfs-progs
sudo apt install smartmontools
wget https://github.com/svanichkin/Netgear-Stora-Replacement-Kit/tree/main/disk/check_disk.sh
mv check_disk.sh /usr/local/bin/
chmod +x /usr/local/bin/check_disk.sh
```

We'll add a reaction to inserted disks, so we'll modify the file.
```
sudo nano /etc/udev/rules.d/99-check-disk.rules
```

And we will add the following line to it.
```
ACTION=="add", KERNEL=="sd[a-z]", RUN="/usr/local/bin/check_disk.sh /dev/%k"
```

Then we will restart the service.
```
udevadm control --reload-rules
udevadm trigger
```