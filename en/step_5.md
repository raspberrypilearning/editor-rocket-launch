<h2 class="c-project-heading--task">Draw the rocket</h2>

--- task ---

Make the rocket appear on the screen.

--- /task --- 

--- task ---

First add `rocket_position` to start at 400 (the screen height). 

Then add another `image()` and use `rocket_position` as the y coordinate.

--- /task ---

--- task ---

Move your rocket and change it to the size you want by editing the code.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 4
line_highlights: 5, 22-23 
---
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
    # Draw background
    background(0, 0, 0)

    # Planet
    image(planet, width/2, 400, 300, 300)

    # Rocket
    image(rocket, width/2, rocket_position, 64, 64)    
  

--- /code ---

--- task ---

**Test:** Run your code and check that the rocket appears.


--- /task ---

</div>


