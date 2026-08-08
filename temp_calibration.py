import os
import time
from sense_hat import SenseHat

sense = SenseHat()
def get_calibrated_temp():

        # Get raw temperature from the Sense HAT sensors
        t_num = sense.get_temperature_from_pressure()

        # Read the Raspberry Pi internal CPU temperatures
        res = os.popen('vcgencmd measure_temp').readline()
        t_cpu = float(res.replace("temp=", "").replace("'C\n",""))

#Calculate calibrated ambient temperature using an offset formula
#(Tyically, ambient is raw temp minus 1/5th of CPU temp)
        t_calibrated = t_num - ((t_cpu - t_num)/5.4)
        return t_calibrated

print(f"Calibrated Temp: {get_calibrated_temp():.2f}C")
