from sense_hat import SenseHat

sense = SenseHat()
r = (255,0,0)
b = (0,0,0)

# Set up where each color will display
creeper_pixels = [
        b, b, b, b, b, b, b, b,
        b, r, r, b, r, r, b, b,
        r, r, r, r, r, r, r, b,
        r, r, r, r, r, r, r, b,
        b, r, r, r, r, r, b, b,
        b, b, r, r, r, b, b, b,
        b, b, b, r, b, b, b, b,
        b, b, b, b, b, b, b, b
]

# Display these colors on the LED matrix
sense.set_pixels(creeper_pixels)
