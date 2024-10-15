#!/usr/bin/env python3

import lgpio
import time
import subprocess
import re

TARGET_GPIO = 18
PWM_FREQUENCY = 10000
OFF_THRESHOLD = 40
FULL_SPEED_THRESHOLD = 65
SAMPLE_TIME = 5
SAMPLE_INTERVAL = 1

def get_all_gpiochips():
    try:
        gpiodetect_output = subprocess.check_output(["gpiodetect"]).decode().strip().splitlines()
        gpiochips = []
        for line in gpiodetect_output:
            match = re.match(r"gpiochip(\d+)", line)
            if match:
                gpiochips.append(match.group(1))
        return gpiochips
    except subprocess.CalledProcessError as e:
        print("Error executing gpiodetect:", e)
        return []

def find_gpiochip_for_gpio(gpio_number):
    gpiochips = get_all_gpiochips()
    if not gpiochips:
        print("No gpiochips found.")
        return None
    try:
        for chip in gpiochips:
            gpioinfo_output = subprocess.check_output(["gpioinfo", f"gpiochip{chip}"]).decode().strip().splitlines()
            for line in gpioinfo_output:
                if f"GPIO{gpio_number}" in line:
                    return chip

        print(f"GPIO {gpio_number} not found in any gpiochip.")
        return None

    except subprocess.CalledProcessError as e:
        print("Error executing gpioinfo:", e)
        return None

gpiochip = find_gpiochip_for_gpio(TARGET_GPIO)
if gpiochip is None:
    print("Not found gpiochip for GPIO", TARGET_GPIO)
    exit(1)

h = lgpio.gpiochip_open(int(gpiochip))

try:
    lgpio.gpio_claim_output(h, TARGET_GPIO)

    def get_temp():
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            temp_str = f.read()
        return int(temp_str) / 1000

    def set_fan_speed(speed):
        print(speed)
        if speed <= 0:
            lgpio.tx_pwm(h, TARGET_GPIO, PWM_FREQUENCY, 0)
        else:
            lgpio.tx_pwm(h, TARGET_GPIO, PWM_FREQUENCY, min(speed, 1)  * 100)

    temperatures = []

    while True:
        temp = get_temp()
        temperatures.append(temp)

        if len(temperatures) >= SAMPLE_TIME:
            average_temp = sum(temperatures) / len(temperatures)
            temperatures = []
            set_fan_speed((average_temp - OFF_THRESHOLD) / (FULL_SPEED_THRESHOLD - OFF_THRESHOLD))

        time.sleep(SAMPLE_INTERVAL)

except KeyboardInterrupt:
    pass
finally:
    lgpio.gpiochip_close(h)