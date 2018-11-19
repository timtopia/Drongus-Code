class MotorController:
  FRONT_LEFT = 1
  FRONT_RIGHT = 2
  BACK_LEFT = 3
  BACK_RIGHT = 4

  throttle = 1

  def __init__(self):
    print ("Hello")

  def set_motor (self, port, value):
    print("MOTOR ", port, " has ", value)

  def set_motors(self, fl, fr, bl, br):
      self.set_motor(self.FRONT_LEFT, fl)
      self.set_motor(self.FRONT_RIGHT, fr)
      self.set_motor(self.BACK_LEFT, bl)
      self.set_motor(self.BACK_RIGHT, br)

  def yaw(self, speed): # -1 <= speed <= 1
    throttle = self.throttle
    self.set_motors(throttle + speed , throttle - speed, throttle - speed, throttle + speed)

  def pitch(self, speed):
    throttle = self.throttle
    self.set_motors(throttle - speed, throttle - speed, throttle + speed, throttle + speed)

  def roll(self, speed):
    throttle = self.throttle
    self.set_motors(throttle + speed, throttle - speed, throttle + speed, throttle - speed)

  def thrust(self, speed):
    throttle = self.throttle
    self.set_motors(throttle + speed, throttle + speed, throttle + speed, throttle + speed)
