from sense_hat import SenseHat

sense = SenseHat()
sense.clear()


amber = (255, 100, 0)

temperature = sense.get_temperature()
temperature = round(temperature, 2)
print(temperature)

sense.show_message(str(temperature)+ " C", text_colour = amber )
