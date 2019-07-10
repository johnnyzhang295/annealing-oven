import time
import adafruit_max31855

class Thermocouple:
    
    def __init__(self):
        #setup stuff
        CLK = 25
        CS = 24
        DO = 18
        self.sensor = adafruit_max31855.MAX31855(CLK, CS, DO)
        self.tempC = 0
        
    def Start(self):
        while True:
            tempC = self.sensor.readTempC()
            print('Temperature: {} C'.format(tempC))
            
            time.sleep(2.0)
            
    def Stop():
        pass

    def GetTempC(self):
        return self.tempC
