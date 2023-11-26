# Required modules are imported and set up
import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
  
# Here the input pin is declared to which the sensor is connected. Additionally the PullUP resistor is activated at the input.
GPIO_PIN = 27
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
  
print ("Sensor test [press CTRL+C to finish the test]")
  
# This output function is executed when a signal is detected
def ausgabeFunktion(null):
        print("Signal detected")
  
# When a signal is detected (falling signal edge) the output function is executed
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=ausgabeFunktion, bouncetime=100) 
  
# Main program loop
try:
        while True:
                time.sleep(1)
  
# Clean up after the program is finished
except KeyboardInterrupt:
        GPIO.cleanup()