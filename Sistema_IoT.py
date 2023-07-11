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
light_sensor = 1


p = int(grovepi.analogRead(potentiometer)/204.5)
now = datetime.datetime.now()
formatted_date = now.strftime("%d/%m/%y/%H:%M:%S")
        
button_status = digitalRead(button)
light_intensity = grovepi.analogRead(light_sensor)
# check if we have nans
# if so, then raise a type error exception
[ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
print("temp =", temp, "C\thumidity =", hum,"%")
print(p)