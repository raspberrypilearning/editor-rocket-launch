from p5 import *
from random import randint

# Define variables
rocket_position = 400

def setup():
    # Set up your animation here
    size(400, 400)
    image_mode(CENTER)
    global planet, rocket
    planet = load_image('planet.png')
    rocket = load_image('rocket.png')

def draw():
    # Re-draw background
    background(0, 0, 0)
    
    # Planet
    image(planet, width/2, 400, 300, 300)    
    
    # Rocket 
    global rocket_position
    rocket_position = rocket_position - 1    
    image(rocket, width/2, rocket_position, 64, 64)     
  #  no_stroke()
    fill(200, 200, 200, 100) 
    for i in range(20):
        ellipse(width/2 + randint(-5,5), rocket_position + randint(20,50), randint(5,10))    

run()