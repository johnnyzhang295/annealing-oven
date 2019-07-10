import time
import adafruit_max31855

class Thermocouple:
    tempC = 0
    CS = 24
    CLK = 25
    
    DO = 18
    def Setup():
        #setup stuff
        sensor = adafruit_max31855.MAX31855(CLK, CS, DO)
        
    def Start():
        while True:
            this.tempC = sensor.readTempC()
            print('Temperature: {} C'.format(this.tempC))
            
            time.sleep(2.0)
            
    def Stop():
        pass