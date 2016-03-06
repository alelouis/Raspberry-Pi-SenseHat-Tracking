import csv
import time
import os
from sense_hat import SenseHat

sense = SenseHat()
filename = "/var/www/html/sense/logs/" + time.strftime("%d_%m_%Y") + '.csv'
print(os.path.abspath(filename))
if(os.path.isfile(filename)):
    print ("Appending log : " + filename);
    with open(filename, 'a') as csvfile:
        fieldnames = ['date','time', 'temperature', 'humidity', 'pressure']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        temp = str(round(sense.temp,1))
        time.sleep(1)
        humidity = str(round(sense.humidity,1))
        time.sleep(1)
        pressure = str(round(sense.pressure,1))
        if(float(temp)>0):
            writer.writerow({'date': time.strftime("%d/%m/%Y"),
                            'time':time.strftime("%H:%M:%S"),
                            'temperature': temp,
                            'humidity': humidity,
                            'pressure': pressure})
else:
    print ("Creating log : " + filename);
    with open(filename, 'w') as csvfile:
        fieldnames = ['date','time', 'temperature', 'humidity', 'pressure']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        temp = str(round(sense.temp,1))
        time.sleep(1)
        humidity = str(round(sense.humidity,1))
        time.sleep(1)
        pressure = str(round(sense.pressure,1))
        if(float(temp)>0):
            writer.writerow({'date': time.strftime("%d/%m/%Y"),
                            'time':time.strftime("%H:%M:%S"),
                            'temperature': temp,
                            'humidity': humidity,
                            'pressure': pressure})
