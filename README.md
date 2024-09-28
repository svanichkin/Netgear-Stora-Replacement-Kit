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

### Prototype V.1

![Main plate V.1](https://raw.githubusercontent.com/svanichkin/Netgear-Stora-Replacement-Kit/refs/heads/main/Photos/Prototype_v.1/5.prototype_plate_v.1.heic)