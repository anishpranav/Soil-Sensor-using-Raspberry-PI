import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
sensor_pin = 17
GPIO.setup(sensor_pin, GPIO.IN)
try:
  while True:
    if GPIO.input(sensor_pin) == GPIO.LOW:
      print("Water detected")
    else:
      print("No water detected")
  time.sleep(1)
except KeyboardInterrupt:
  print("Program terminated by user")
finally:
  GPIO.cleanup()