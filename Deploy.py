import RPi.GPIO as GPIO
import smbus2 as smbus
import GPS_ard_py as gps



def read_acceration():
    bus = smbus.SMBus(0)
    data = bus.read_i2c_block_data(0x67, 0x00, 1, force=None)
    parseInt = data[0]
    return parseInt

def deploy(pin:int, height:float):
    position = gps.read_gps_data()
    latitude, longuitude, altitude, horizontal_dil = position
    if(read_acceration() > 0.8 and altitude > height):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)    
        GPIO.output(pin, GPIO.HIGH)

