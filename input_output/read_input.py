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
            # 'num_balls': self.num_balls
        }
        return info

    def get_input(self):
        # Return a dictionary containing the current state of the joystick.
        pygame.event.pump()
        time = pygame.time.get_ticks()
        axes = [self.joystick.get_axis(i) for i in range(self.num_axes)]
        buttons = [self.joystick.get_button(i) for i in range(self.num_buttons)]
        hats = [list(self.joystick.get_hat(i)) for i in range(self.num_hats)]
        # remove list to go back to original
        # 'balls': [self.joystick.get_ball(i) for i in range(self.num_balls)]
        data = {
            "time": time,
            "axis_0": axes[0],
            "axis_1": axes[1],
            "axis_2": axes[2],
            "axis_3": axes[3],
            "axis_4": axes[4],
            "button_0": buttons[0],
            "button_1": buttons[1],
            "button_2": buttons[2],
            "button_3": buttons[3],
            "button_4": buttons[4],
            "button_5": buttons[5],
            "button_6": buttons[6],
            "button_7": buttons[7],
            "button_8": buttons[8],
            "button_9": buttons[9],
            "button_10": buttons[10],
            "button_11": buttons[11],
            "hat_0": (hats[0][0], hats[0][1]),
        }
        return data


