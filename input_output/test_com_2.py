import json
import socket
import pygame
from read_input import Joystick
import time

pygame.init()
joystick_id = 0

# Create joystick instance
joystick = Joystick(joystick_id)

"""
AXIS 2 -> THROTTLE
AXIS 3 -> YAW
AXIS 1 -> PITCH
AXIS 0 -> ROLL
"""


def get_input_data():
    # Handle joystick events
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN:
            # Get input data from joystick
            input_data = joystick.get_input()

            # Convert input data to a JSON string
            json_data = json.dumps(input_data).encode('utf-8')

            return json_data

    # Wait for a short time to avoid overloading the system
    time.sleep(0.0001)
    return None


# Create a socket connection to Rust
HOST = 'localhost'
PORT = 3333
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("connected")

    # Loop forever
    while True:
        # Get input data from joystick
        json_data = get_input_data()
        if json_data:
            # Send input data to Rust
            s.sendall(json_data)

        # Wait for a short time to avoid overloading the system
        time.sleep(0.0001)

