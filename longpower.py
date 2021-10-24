#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

KEY = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY, GPIO.OUT)
GPIO.output(KEY, GPIO.LOW)

timeout = 5

GPIO.output(KEY, GPIO.HIGH)
time.sleep(timeout)
GPIO.output(KEY, GPIO.LOW)

