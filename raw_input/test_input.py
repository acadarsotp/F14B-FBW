import csv
import pygame
from read_input import Joystick
from threading import Thread
import time

pygame.init()
joystick_id = 0

"""
AXIS 2 -> THROTTLE
AXIS 3 -> YAW
AXIS 1 -> PITCH
AXIS 0 -> ROLL
"""


def write_csv():
    with open('joystick_input.csv', mode='w', newline='') as csv_file:
        # Create CSV writer
        writer = csv.writer(csv_file)

        # Write header row
        joystick = Joystick(joystick_id)
        joystick_info = joystick.get_info()
        axes = joystick_info['num_axes']
        buttons = joystick_info['num_buttons']
        hats = joystick_info['num_hats']
        header = ['time'] + [f'axis {i}' for i in range(axes)] + \
                 [f'button {i}' for i in range(buttons)] + \
                 [f'hat {i}' for i in range(hats)] + \
                 [f'ball {i}' for i in range(joystick_info['num_balls'])]
        writer.writerow(header)

        while True:
            # Get input data from joystick
            input_data = joystick.get_input()

            # Write input data to CSV file
            row = [input_data['time']] + input_data['axes'] + \
                  input_data['buttons'] + input_data['hats'] + \
                  input_data['balls']
            writer.writerow(row)

            time.sleep(0.0001)


# Create a separate thread for writing to the CSV file
write_thread = Thread(target=write_csv)
write_thread.start()

# Create joystick instance
joystick = Joystick(joystick_id)

# Loop forever
while True:
    # Handle joystick events
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN:
            # Get input data from joystick
            input_data = joystick.get_input()

    # Wait for a short time to avoid overloading the system
    time.sleep(0.0001)
