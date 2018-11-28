class MotorController:
  FRONT_LEFT = 1
  FRONT_RIGHT = 2
  BACK_LEFT = 3
  BACK_RIGHT = 4
  motor_vals = [0,0,0,0]

  hover = 0.5

  def __init__(self):
    print ("Hello")

  def set_motor (self, port, value):
    #print("MOTOR ", port, " has ", value)
    self.motor_vals[port-1] += value

  def set_motors(self, fl, fr, bl, br):
      self.set_motor(self.FRONT_LEFT, fl)
      self.set_motor(self.FRONT_RIGHT, fr)
      self.set_motor(self.BACK_LEFT, bl)
      self.set_motor(self.BACK_RIGHT, br)

  def yaw(self, speed): # -1 <= speed <= 1
    self.set_motors(speed, -speed, -speed, speed)

  def pitch(self, speed):
    self.set_motors(-speed, -speed, speed, speed)

  def roll(self, speed):
    self.set_motors(speed, -speed, speed, -speed)

  def thrust(self, speed):
    self.set_motors(speed, speed, speed, speed)

  def display(self):
    fl, fr, bl, br = self.motor_vals
    print("{}\t\t{}\n\n{}\t\t{}".format(fl, fr, bl, br))

  def reset(self):
    self.motor_vals = [self.hover, self.hover, self.hover, self.hover]    
