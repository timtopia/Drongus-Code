FRONT_LEFT = 1
FRONT_RIGHT = 2
BACK_LEFT = 3
BACK_RIGHT = 4

throttle = 1

def set_motor (port, value):
  print("MOTOR ", port, " has ", value)

def set_motors(fl, fr, bl, br):
    set_motor(FRONT_LEFT, fl)
    set_motor(FRONT_RIGHT, fr)
    set_motor(BACK_LEFT, bl)
    set_motor(BACK_RIGHT, br)

def yaw(speed): # -1 <= speed <= 1
  set_motors(throttle + speed , throttle - speed, throttle - speed, throttle + speed)

def pitch(speed):
  set_motors(throttle - speed, throttle - speed, throttle + speed, throttle + speed)

def roll(speed):
  set_motors(throttle + speed, throttle - speed, throttle + speed, throttle - speed)
