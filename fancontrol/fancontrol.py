#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO_PIN = 18
PWM_FREQUENCY = 25000

OFF_THRESHOLD = 40
FULL_SPEED_THRESHOLD = 65
SAMPLE_TIME = 5
SAMPLE_INTERVAL = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

pwm = GPIO.PWM(GPIO_PIN, PWM_FREQUENCY)

def get_temp():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp_str = f.read()
    return int(temp_str) / 1000

def set_fan_speed(speed):
    if speed <= 0:
        pwm.stop()
    else:
        pwm.start(min(speed, 1)  * 100)

try:
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
    pwm.stop()
    GPIO.cleanup()