from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temperature = sense.get_temperature()
temperature = round(temperature, 2)
print(temperature)

sense.show_message(str(temperature)+ " C" )
