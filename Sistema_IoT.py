import grovepi 
import csv
import numpy as np
from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import datetime

button = 2
dht_sensor_port = 3
dht_sensor_type = 0 

button_status = digitalRead(button)
light_intensity = grovepi.analogRead(light_sensor)