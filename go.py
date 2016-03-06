#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import max7219.led as led
import RPi.GPIO as GPIO
import sys
import time
import serial
import datetime
import Adafruit_DHT
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT
from random import randrange
from time import sleep

device = led.matrix(cascaded=20, spi_bus=0, spi_device=0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, True)

time_H_old = 0
time_M_old = 0
time_S_old = 0

ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate = 9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.5
)
counter=0

nowtime = time.strftime("%H:%M:%S")
print nowtime

# while True:
#     device.brightness(7)
#     device.orientation(0)
#     nowtime = time.strftime("%H:%M:%S")
#     device.show_message(nowtime)

# while True:
#     device.brightness(7)
#     device.orientation(0)
#     time_H = time.strftime("%H")
#     time_M = time.strftime("%M")
#     time_S = time.strftime("%S")
#     print time_H,":",time_M,":",time_S

device.brightness(7)
# device.orientation(0)

while True:
    device.letter(17, ord(':'))
    
    time_H = time.strftime("%H")
    j = 15
    k = 0
    for i in (time_H):
        if (i == "0" and k == 0):
            i = " "
        device.letter(j, ord(i))
        j += 1
        k += 1
     
    time_M = time.strftime("%M")
    j = 18
    for i in (time_M):
        device.letter(j, ord(i))
        j += 1
            
    time_S = time.strftime("%S")
    j = 5
    k = 0
    for i in (time_S):
        if (i == "0" and k == 0):
            i = " "
        device.letter(j, ord(i))
        j += 1
        k += 1

    if (time_S != time_S_old):
        time_S_old = time_S
        print time_H,":",time_M,":",time_S
#         humidity, temperature = Adafruit_DHT.read_retry(22, 26)
#         print humidity
#         print temperature
#         x = float(ser.readline())
#         print x
#         light = int((x/1024)*16)
#         print light
#         device.brightness(light)
 