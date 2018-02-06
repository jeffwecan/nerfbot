#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code for Adafruit 16 channel PWM Driver
# Refactored by ruprecht
# Numbers for HS-55 Servo (20ms/50Hz cycle, 1000-2000 us width)
# ===========================================================================
1
# Initialise the PWM device using the default address 0x40
pwm = PWM(0x40, debug=True)

servoMin = 1000  # Min pulse length, us (tick 184/4096)
servoMax = 2000  # Max pulse length, us  (tick 430/4096)
servoMid = servoMax - ((servoMax-servoMin)/2) # Midpoint pulse length, us
cycle = 50 # cycle length, Hz

pulseLength = 1000000 / cycle
tick = pulseLength / 4096 # 12 bit resolution

# we need to convert us pulses to 12 bit ticks
def setServoPulse(channel, pulse):
  pwm.setPWM(channel, 0, pulse/tick)

pwm.setPWMFreq(cycle) # Set frequency

while (True):
  # cycle servo
  setServoPulse(0, servoMin)
  time.sleep(1)
  setServoPulse(0, servoMid)
  time.sleep(1)
  setServoPulse(0, servoMax)
  time.sleep(1)

import RPi.GPIO as GPIO
import time

servo_pin = 5
duty_cycle = 7.5     # Should be the centre for a SG90

# Configure the Pi to use pin names (i.e. BCM) and allocate I/O
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create PWM channel on the servo pin with a frequency of 50Hz
pwm_servo = GPIO.PWM(servo_pin, 50)
pwm_servo.start(duty_cycle)

try:
    while True:
        duty_cycle = float(input("Enter Duty Cycle (Left = 5 to Right = 10):"))
        pwm_servo.ChangeDutyCycle(duty_cycle)

except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
