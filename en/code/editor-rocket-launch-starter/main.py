from p5 import *
from random import randint

# Define variables

def setup():
    # Set up your animation here
    size(400, 400)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image('planet.png')
    rocket = load_image('rocket.png')

def draw():


run() # Keep this to run your code