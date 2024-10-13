# Power off button

When the button on the board is pressed, the board's controller sends an I2C signal to the GPIO. Then we receive this signal and perform a shutdown. After that, the controller waits for 30 seconds and then cuts the power. Additionally, the script is configured with a period of 180 seconds, after which the power will be turned off, followed by a power-on cycle after 60 seconds. This might happen if the controller loses communication over I2C, for example, if something freezes.

First, we will install the original binary file for PiWatcher, then we will connect the script for autostart.

```
wget -N http://omzlo.com/downloads/aarch64/piwatcher
sudo chmod a+x piwatcher
sudo mv piwatcher /usr/local/bin/
wget https://github.com/svanichkin/Netgear-Stora-Replacement-Kit/tree/main/piwatcher/piwatcher.py
sudo chmod a+x piwatcher.sh
mkdir /home/piwatcher/
sudo mv piwatcher.py /home/piwatcher/
```

Now let's add the script to autostart using systemd
```
wget https://github.com/svanichkin/Netgear-Stora-Replacement-Kit/tree/main/piwatcher/piwatcher.service
sudo mv piwatcher.service /etc/systemd/system/
sudo systemctl enable piwatcher.service
sudo systemctl start piwatcher.service
```


