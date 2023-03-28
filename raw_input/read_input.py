import pygame


class Joystick:
    def __init__(self, joystick_id=0):
        self.joystick = pygame.joystick.Joystick(joystick_id)
        self.joystick.init()
        self.num_axes = self.joystick.get_numaxes()
        self.num_buttons = self.joystick.get_numbuttons()
        self.num_hats = self.joystick.get_numhats()
        self.num_balls = self.joystick.get_numballs()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.joystick.quit()

    def get_info(self):
        """Return a dictionary containing information about the joystick."""
        info = {
            'name': self.joystick.get_name(),
            'num_axes': self.num_axes,
            'num_buttons': self.num_buttons,
            'num_hats': self.num_hats,
            'num_balls': self.num_balls
        }
        return info

    def get_input(self):
        """Return a dictionary containing the current state of the joystick."""
        pygame.event.pump()

        data = {
            'time': pygame.time.get_ticks(),
            'axes': [self.joystick.get_axis(i) for i in range(self.num_axes)],
            'buttons': [self.joystick.get_button(i) for i in range(self.num_buttons)],
            'hats': [self.joystick.get_hat(i) for i in range(self.num_hats)],
            'balls': [self.joystick.get_ball(i) for i in range(self.num_balls)]
        }

        return data
