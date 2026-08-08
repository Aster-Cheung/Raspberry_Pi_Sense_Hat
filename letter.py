from sense_hat import SenseHat

MySH = SenseHat()
#MySH.low_light = True

green = (0,25, 0)
a = input('Enter a letter:')
MySH.show_letter(a, text_colour = green)
