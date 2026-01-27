<h2 class="c-project-heading--task">Draw the rocket</h2>

--- task ---

Add another `image()` function to make the rocket appear on the screen.

Add the variable `rocket_position` to start at 400 (the screen height) and use `rocket_position` as the rocket `image` y coordinate.

--- /task --- 


<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 5, 20 
---
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
    # Make your animation here
    background(0, 0, 0)
    image(planet, width/2, 400, 300, 300)
    image(rocket, width/2, rocket_position, 64, 64)    

--- /code ---

--- task ---

**Test:** Run your code and check that the rocket appears.

Move your rocket and change it to the size you want by editing the code.

--- /task ---

</div>


