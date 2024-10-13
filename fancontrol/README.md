# Fan control

The fan is connected to GPIO 18 (PWM) and GPIO 24 (RPM), allowing you to both read the fan speed and control its rotation speed. To do this, a script is required. This script can also be added to the device's autostart.

First, we need to install some packages to make this work.

```
sudo apt install python3-gpiozero
wget https://github.com/svanichkin/Netgear-Stora-Replacement-Kit/tree/main/fancontrol/fancontrol.py
sudo mv fancontrol.py /usr/local/bin/fancontrol.py
sudo chmod +x /usr/local/bin/fancontrol.py
```

Now let's add the script to autostart using systemd
```
wget https://github.com/svanichkin/Netgear-Stora-Replacement-Kit/tree/main/fancontrol/fancontrol.service
sudo mv fancontrol.service /etc/systemd/system/fancontrol.service
sudo systemctl enable fancontrol.service
sudo systemctl start fancontrol.service
```

