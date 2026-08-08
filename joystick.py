# Initialize SenseHat instance
# This tutorial code shows you how to move an LED dot to the right when a right joystick action is made

from sense_hat import SenseHat
sense = SenseHat()

# Intialization
sense.clear()
x = 3
y = 3
sense.set_pixel(x, y, 250, 250, 250)
Done = False


while (Done == False):
  event = sense.stick.wait_for_event()
  if event.direction == "left":
    if event.action == "pressed":
      if x == 0:
        x = 7
      else:
        x = x-1
  
  elif event.direction == "right":
    if event.action == "pressed":
      if x == 7:
        x = 0
      else:
        x = x+1
        
  elif event.direction == "up":
    if event.action == "pressed":
      if y == 7:
        x = 7
      else:
        y = y-1
        
  elif event.direction == "down":
    if event.action == "pressed":
      if y == 7:
        x = 0
      else:
        y = y+1
    
  else:
      Done = True
      sense.show_message('Program terminated', text_colour = [250, 250, 250])
      
sense.clear()
sense.set_pixel(x, y, 250, 250, 250)
