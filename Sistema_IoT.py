import grovepi 
import csv
import numpy as np
from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import datetime

def collect_sensor_data():
    button = 2
    potentiometer = 2
    light_sensor = 1
    dht_sensor_port = 3
    dht_sensor_type = 0 
    
    grovepi.pinMode(potentiometer,"INPUT")
    
    data = []  # Lista para almacenar los datos recopilados
    
    while True:
        try:
            p = int(grovepi.analogRead(potentiometer)/204.5)
            now = datetime.datetime.now()
            formatted_date = now.strftime("%d/%m/%y/%H:%M:%S")
                    
            button_status = digitalRead(button)
            light_intensity = grovepi.analogRead(light_sensor)
            
            [temp, hum] = dht(dht_sensor_port, dht_sensor_type)
            print("temp =", temp, "C\thumidity =", hum, "%")
            print(p)
    
            if isnan(temp) is True or isnan(hum) is True:
                raise TypeError('nan error')
            
            t = str(temp)
            h = str(hum)
            l = str(light_intensity)
            pt = str(p)
    
            if button_status:
                setText_norefresh("Temp:" + t + "C\n" + "Humidity:" + h + "%")
                sleep(0.5)
            else:
                setText_norefresh("light:" + l + "\n" + "Time:" + pt +"s")
                sleep(0.5)
                    
            filename = "tabla.csv"
                
            with open(filename, mode="a") as file:
                writer = csv.writer(file)
                writer.writerow([formatted_date, t, h, l])
                time.sleep(p)
            print("Datos guardados en", filename)
            
            # Agregar los datos recopilados a la lista
            data.append((formatted_date, temp, hum, light_intensity))
            
        except (IOError, TypeError) as e:
            print(str(e))
            setText("")
            
        except KeyboardInterrupt as e:
            print(str(e))
            setText("")
            break
        sleep(0.5)
    
    return data