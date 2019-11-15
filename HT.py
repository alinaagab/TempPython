from sense_hat import SenseHat
sense = SenseHat()


blue = (0, 0, 255)
red = (255,0,0)

while True:

  
  t = sense.get_temperature()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  h = round(h, 1)
  
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t)  + " Humidity: " + str(h)
  
  if t > 18.3 and t < 26.7:
    bg = blue
  else:
    bg = red
  

  sense.show_message(message, scroll_speed=0.05, back_colour=bg)
