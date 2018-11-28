import pygame

class Joystick:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joy = pygame.joystick.Joystick(0)
        self.joy.init()

    def update(self):
        pygame.event.get()
        
        values = {}
        values["LEFT_X"] = self.joy.get_axis(0)
        values["LEFT_Y"] = self.joy.get_axis(1)
        values["RIGHT_X"] = self.joy.get_axis(2)
        values["RIGHT_Y"] = -self.joy.get_axis(3)

        hat = self.joy.get_hat(0)
        values["HAT_X"] = hat[0]
        values["HAT_Y"] = hat[1]

        buttons = ["X","A","B","Y","LB","RB","LT","RT","BACK","START","LSTICK","RSTICK"]
        for i in range(len(buttons)):
            values[buttons[i]] = self.joy.get_button(i)

        for i in values:
            if abs(values[i]) < 0.1:
                values[i] = 0

        return values
    
        
