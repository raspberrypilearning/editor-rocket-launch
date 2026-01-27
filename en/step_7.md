<h2 class="c-project-heading--task">Blast off!</h2>

--- task ---

Move the rocket up the screen to create an animation.

--- /task --- 

--- task ---

In `draw()` decrease `rocket_position` by 1 each time a new frame is drawn. This moves the image to a new y coordinate, making the animation.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 15 
line_highlights: 20
---
def draw():
    # Make your animation here
    global rocket_position
    background(0, 0, 0)
    
    # Planet
    image(planet, width/2, 400, 300, 300)    
    
    # Rocket 
    rocket_position = rocket_position - 1    
    image(rocket, width/2, rocket_position, 64, 64)     
--- /code ---

--- test ---

**Test:** Run your code to check that the rocket blasts off from the bottom of the screen.

--- /test ---
</div>

<div class="c-project-output">
![A rocket flying at a steady speed from the bottom to the top of the screen.](images/fly.gif){:width="300px"}
</div>