import serial 
from datetime import datetime

with open('GPS_nav_data', 'w') as file:
    file.write('GPS NAV DATA')
    file.write("GPS NAVIGATION DATA DATE:" + datetime.today().strftime('%Y-%m-%d'))

with serial.Serial('/dev/serial0') as ser:
    ser.baudrate = 115200
    text = ser.read()

while True:
    text = ser.read()
    alt = round(text/1000, 1)
    lat = round(text/100 - alt, 1)
    lon = round(text/10- alt - lat,1)    
    
    print('altitude+ '+ alt + 'latitude'+ lat + 'longuitude' + lon)
    file.writelines('altitude+ '+ alt + 'latitude'+ lat + 'longuitude' + lon)
    
    
    