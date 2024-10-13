# Netgear Stora → Replacement Kit

This project is designed for Netgear Stora MS2000 owners to allow them to use their NAS indefinitely. A new board has been created that replaces the old one, retaining all the original functions except for computing capabilities, and allows you to enhance your Stora’s performance.

### New Board Features

- **Board Type**: Proxy Board
- **Functions**: Retains all original board functions (Reset, PowerOn, Ethernet) except for computing
- **Supported Computing Boards**: Raspberry Pi Zero, Raspberry Pi 5, Radxa, Beagle, Orange Pi, and others
- **Buttons**: Reset, PowerOn
- **Ports**: Ethernet, front panel USB
- **LED Indicators**: Power, 2xHDD LEDs

### Proxy Board Advantages

- **Configuration Flexibility**: Ability to use various computing boards to configure the NAS performance.
- **Operating System Support**: OMV, FreeNAS, Linux (Ubuntu, Debian, Raspbian), BSD, Plan9.
- **Ethernet**: Direct connection to the computing board, providing speeds from 100 Mbps to 10 Gbps.
- **RAM**: Ability to install up to 32 GB of RAM using the appropriate module.

### Additional Components

- **GPIO Adapter**: Included for connecting the computing board to the proxy board.
- **USB → SATA Adapters**: For connecting HDDs via the proxy board.
- **Fan**: 4-pin and 5V, such as the Noctua NF-A6x25 5V PWM.

### Power Management

- **Power Controller**: Built on the PiWatcher base (https://github.com/omzlo/piwatcher) and fully compatible with it.
- **Controller Functions**: Manages the computing board via GPIO, controls 12V and 3.3V power.
- **Automatic Recovery**: After an emergency power outage, the board automatically turns on and supplies power to the computing board.
- **Pin-out**: 12V, 3.3V, 5V for connecting additional modules.

### SATA Connection

- **HDD Slots**: HDDs are inserted into standard slots, SATA is proxied inside the device and available to the computing board.
- **HDD Power**: Provides 12V, 3.3V, 5V power for each drive.

This kit allows Netgear Stora MS2000 users to upgrade and modernize their device, providing the possibility of flexible configuration and supporting modern computing power.

## Fan control

Our device uses GPIO 18 to control the fan speed. This script does it based on the device's temperature. Here is the instruction for installing this script: 
https://github.com/svanichkin/Netgear-Stora-Replacement-Kit/blob/main/fancontrol/README.md

## Power off button

Our board contains components and firmware from the Piwatcher project (https://www.omzlo.com/articles/the-piwatcher), which allows for power management. If the power button is held for more than two seconds, Piwatcher controller will forcefully cut the power. If we need a soft shutdown with a brief press of the power button, we will need to add a script that reads the button press. https://github.com/svanichkin/Netgear-Stora-Replacement-Kit/blob/main/piwatcher/README.md

## Disk auto format

When we insert a disk, the system should recognize it. If it is a new disk, it needs to be prepared.
https://github.com/svanichkin/Netgear-Stora-Replacement-Kit/blob/main/disk/README.md

### Prototype V.1

![Main plate V.1](https://raw.githubusercontent.com/svanichkin/Netgear-Stora-Replacement-Kit/refs/heads/main/Photos/Prototype_v.1/5.prototype_plate_v.1.heic)

## Prototype in box with RPI

![Closed in box](https://raw.githubusercontent.com/svanichkin/Netgear-Stora-Replacement-Kit/refs/heads/main/Photos/Prototype_v.1/1.prototype_nas_v.1.jpg)

![Closed in box](https://raw.githubusercontent.com/svanichkin/Netgear-Stora-Replacement-Kit/refs/heads/main/Photos/Prototype_v.1/2.prototype_nas_v.1.jpg)

![Opened box](https://raw.githubusercontent.com/svanichkin/Netgear-Stora-Replacement-Kit/refs/heads/main/Photos/Prototype_v.1/3.prototype_nas_v.1.jpg)

![Opened box](https://raw.githubusercontent.com/svanichkin/Netgear-Stora-Replacement-Kit/refs/heads/main/Photos/Prototype_v.1/4.prototype_nas_v.1.jpg)


## Testing

### Off → Plugged into the outlet OR restart after power loss
- [x] OFF → ON controller, power on GPIO, LED, FAN
- [x] 0V → 5V at GPIO input
- [x] OFF → ON power LED indicator
- [x] 0V → 5V FAN
- [x] OFF → ON controller, power on SATA, pinout
- [x] 0V → 3.3V at pinout output
- [x] 0V → 5V at pinout output
- [x] 0V → 12V at pinout output
- [x] 0V → 3.3V data
- [x] 0V → 5V SATA
- [x] 0V → 12V SATA
- [x] RPI I2C send watch 180 → controller set watchdog timer and wait for ping
- [x] RPI I2C send status (ping) while 15 sleep → controller reset watchdog ping timer

### On → Pressed the power button (longer than two seconds)
- [x] ON → OFF controller, power off GPIO, LED, FAN
- [x] 5V → 0V at GPIO input
- [ ] ON → OFF power LED indicator
- [ ] 5V → 0V FAN
- [x] ON → OFF controller, power off SATA, pinout
- [x] 3.3V → 0V at pinout output
- [x] 5V → 0V at pinout output
- [x] 12V → 0V at pinout output
- [x] 0V → 3.3V SATA
- [x] 0V → 5V SATA
- [x] 0V → 12V SATA

### Off → Pressed the power button (briefly)
- [x] OFF → ON controller, power on GPIO, LED, FAN
- [x] 0V → 5V at GPIO input
- [x] OFF → ON power LED indicator
- [x] 0V → 5V FAN
- [x] OFF → ON controller, power on SATA, pinout
- [x] 0V → 3.3V at pinout output
- [x] 0V → 5V at pinout output
- [x] 0V → 12V at pinout output
- [x] 0V → 3.3V SATA
- [x] 0V → 5V SATA
- [x] 0V → 12V SATA
- [x] RPI I2C send watch 180 → controller set watchdog timer and wait for ping
- [x] RPI I2C send status (ping) while 15 sleep → controller reset watchdog ping timer

### On → Pressed the power button (briefly)
- [x] controller I2C send button_pressed → RPI get button_pressed start shutdown script
- [x] RPI disabled, no ping I2C → controller watchdog timer expired
- [x] controller wait 180 seconds → GPIO, LED, FAN power off script
- [x] 5V → 0V at GPIO input
- [ ] ON → OFF power LED indicator
- [ ] 5V → 0V FAN
- [x] controller wait 180 seconds → SATA power off script, pinout
- [x] 3.3V → 0V at pinout output
- [x] 5V → 0V at pinout output
- [x] 12V → 0V at pinout output
- [x] 0V → 3.3V SATA
- [x] 0V → 5V SATA
- [x] 0V → 12V SATA

### On → Power loss, then restored
- [x] Auto power on

### On → Raspberry Pi froze
- [x] Reboot

### Reboot → Pressed the Reset button
- [ ] 5V → 0V at GPIO input

### Reboot → Released the Reset button
- [ ] 0V → 5V at GPIO input

### Operation
- [ ] SATA 1 HDD connected → LED indicator 1 blinks during read/write
- [ ] SATA 2 HDD connected → LED indicator 2 blinks during read/write
- [ ] USB front, plug in flash drive → Flash drive visible in RPI
- [x] Fan RPM reading
- [x] Fan speed control