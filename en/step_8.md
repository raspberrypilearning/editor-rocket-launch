<h2 class="c-project-heading--task">Lots of circles</h2>

--- task ---

➡️ Add a loop to draw multiple circles, to make the exhaust
effect even better.

--- /task ---

Indent the code you used to draw the circle, and add a loop which will run the code 20 times.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 15-22
---

def draw_rocket():
    global rocket_position
    rocket_position = rocket_position - 1
    image(rocket, width/2, rocket_position, 64, 64)
    fill(200, 200, 200, 100) 
    for i in range(20):
        circle_size = randint(5,10)
        ellipse(
            screen_size/2, 
            rocket_position, 
            circle_size,    
            circle_size
        )
    

--- /code ---


<div class="c-project-callout c-project-callout--tip">

### Tip

The `ellipse()` function call is written over multiple lines to make it easier to read. 
</div>

**Test:** Run your program. You will still see a flashing grey circle at the bottom of the rocket - all of the circles have been drawn on top of each other! 
