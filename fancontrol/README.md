# Fan control

The fan is connected to GPIO 18 (PWM) and GPIO 24 (RPM), allowing you to both read the fan speed and control its rotation speed. To do this, a script is required. This script can also be added to the device's autostart.

First, we need to install some packages to make this work.

```
sudo apt update
sudo apt install python3-rpi.gpio
wget https://raw.githubusercontent.com/svanichkin/Netgear-Stora-Replacement-Kit/refs/heads/main/fancontrol/fancontrol.py
sudo mv -f fancontrol.py /usr/local/bin/
sudo chmod a+x /usr/local/bin/fancontrol.py
```

Now let's add the script to autostart using systemd
```
wget https://raw.githubusercontent.com/svanichkin/Netgear-Stora-Replacement-Kit/refs/heads/main/fancontrol/fancontrol.service
sudo mv -f fancontrol.service /etc/systemd/system/
sudo systemctl enable fancontrol.service
sudo systemctl start fancontrol.service
```

