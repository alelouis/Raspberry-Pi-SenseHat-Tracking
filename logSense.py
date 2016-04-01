import csv
import time
import os
from sense_hat import SenseHat

sense = SenseHat()

filename = "/var/www/html/sense/logs/" + time.strftime("%d_%m_%Y") + '_temp.csv'
print(os.path.abspath(filename))
if(os.path.isfile(filename)):
    print ("Appending log : " + filename);
    with open(filename, 'a') as csvfile:
        fieldnames = ['date', 'temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        temp = str(round(sense.temp,1))
        if(float(temp)>0):
            writer.writerow({'date': time.strftime("%Y/%m/%d %H:%M:%S"),
                            'temperature': temp})
else:
    print ("Creating log : " + filename);
    with open(filename, 'w') as csvfile:
        fieldnames = ['date', 'temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        temp = str(round(sense.temp,1))
        if(float(temp)>0):
            writer.writerow({'date': time.strftime("%Y/%m/%d %H:%M:%S"),
                            'temperature': temp})

time.sleep(1)

filename = "/var/www/html/sense/logs/" + time.strftime("%d_%m_%Y") + '_humidity.csv'
print(os.path.abspath(filename))
if(os.path.isfile(filename)):
    print ("Appending log : " + filename);
    with open(filename, 'a') as csvfile:
        fieldnames = ['date', 'humidity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        humidity = str(round(sense.humidity,1))
        if(float(humidity)>0):
            writer.writerow({'date': time.strftime("%Y/%m/%d %H:%M:%S"),
                            'humidity': humidity})
else:
    print ("Creating log : " + filename);
    with open(filename, 'w') as csvfile:
        fieldnames = ['date', 'humidity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        humidity = str(round(sense.humidity,1))
        if(float(humidity)>0):
            writer.writerow({'date': time.strftime("%Y/%m/%d %H:%M:%S"),
                            'humidity': humidity})

time.sleep(1)

filename = "/var/www/html/sense/logs/" + time.strftime("%d_%m_%Y") + '_pressure.csv'
print(os.path.abspath(filename))
if(os.path.isfile(filename)):
    print ("Appending log : " + filename);
    with open(filename, 'a') as csvfile:
        fieldnames = ['date','pressure']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        pressure = str(round(sense.pressure,1))
        if(float(pressure)>0):
            writer.writerow({'date': time.strftime("%Y/%m/%d %H:%M:%S"),
                            'pressure': pressure})
else:
    print ("Creating log : " + filename);
    with open(filename, 'w') as csvfile:
        fieldnames = ['date','pressure']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        pressure = str(round(sense.pressure,1))
        if(float(pressure)>0):
            writer.writerow({'date': time.strftime("%Y/%m/%d %H:%M:%S"),
                            'pressure': pressure})


sense.set_pixel(0,0,0,0,255);
time.sleep(0.1)
sense.set_pixel(0,1,0,255,0);
time.sleep(0.1)
sense.set_pixel(0,2,255,0,0);
time.sleep(0.1)
sense.set_pixel(0,0,0,0,0);
time.sleep(0.1)
sense.set_pixel(0,1,0,0,0);
time.sleep(0.1)
sense.set_pixel(0,2,0,0,0);
