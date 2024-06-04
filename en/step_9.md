<h2 class="c-project-heading--task">Lots of circles</h2>

--- task ---

Generate the circles in random places instead of on top of each other. 

--- /task ---

Generate a random number and add it to the x and y position of each circle so they aren't all drawn in the same place.

--- code ---
---
language: python
line_numbers: true
line_number_start: 16
line_highlights: 17-18
---

ellipse(
    screen_size/2 + randint(-5,5), 
    rocket_position + randint(20,50), 
    circle_size, 
    circle_size
)   

--- /code ---
   

**Test:** Run your program and you should see lots of grey circles in random places at the bottom of the rocket. 
