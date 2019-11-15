from sense_hat import SenseHat
sense = SenseHat()

# Define the colours red and green
blue = (0, 0, 255)
pink = (204,102,153)

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  

  # Round the values to one decimal place
  t = round(t, 1)
  
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) 
  
  if t > 18.3 and t < 26.7:
    bg = blue
  else:
    bg = pink
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05, back_colour=bg)
