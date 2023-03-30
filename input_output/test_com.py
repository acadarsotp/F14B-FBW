import json
import socket
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

# Create a socket connection to Rust
HOST = 'localhost'
PORT = 3333
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def send_input_data(input_data):
    # Convert input data to a JSON string
    json_data = json.dumps(input_data).encode('utf-8')

    # Send the JSON data to Rust
    s.sendall(json_data)


def read_input_data():
    while True:
        # Handle joystick events
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYBUTTONDOWN \
                    or event.type == pygame.JOYBUTTONUP:
                # Get input data from joystick
                input_data = joystick.get_input()

                # Send input data to Rust
                send_input_data(input_data)

        # Wait for a short time to avoid overloading the system
            time.sleep(0.001)


# Create a separate thread for reading joystick input and sending to Rust
input_thread = Thread(target=read_input_data)
input_thread.start()

# Create joystick instance
joystick = Joystick(joystick_id)

# Loop forever
while True:
    # Wait for a short time to avoid overloading the system
    time.sleep(0.0001)
