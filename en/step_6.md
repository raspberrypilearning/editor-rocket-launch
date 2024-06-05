<h2 class="c-project-heading--task">Blast off!</h2>

--- task ---
✅ Each time a new frame is drawn, move the rocket one pixel up the screen to create an animation effect.

![A rocket flying at a steady speed from the bottom to the top of the screen.](images/fly.gif){:width="300px"}

--- /task --- 

The `rocket_position` of the rocket will start at 400 (the screen height) and then decrease by 1 each time a new frame is drawn.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 8 
line_highlights: 11
---

# The draw_rocket function goes here   
def draw_rocket():   
    global rocket_position     
    rocket_position = rocket_position - 1    
    image(rocket, width/2, rocket_position, 64, 64)    
--- /code ---
</div>

**Test:** Run your code to check that the rocket blasts off from the bottom of the screen.

