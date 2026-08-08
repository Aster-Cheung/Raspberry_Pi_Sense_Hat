#Less Bright
from sense_hat import SenseHat

sense = SenseHat()
sense.clear
sense.low_light = True

humidity = sense.get_humidity()
humidity = round(humidity, 2)

print(humidity)

sense.show_message(str(humidity) + " %")
