<h2 class="c-project-heading--task">Random circles</h2>

--- task ---

Generate the circles in random places instead of on top of each other. 

--- /task ---

--- task ---

Change the `randint()` number ranges in your code to make your smoke how you want it.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 22
line_highlights: 28
---
    # Rocket
    global rocket_position
    rocket_position = rocket_position - 1   
    image(rocket, width/2, rocket_position, 64, 64)    
    fill(200, 200, 200, 100) 
    for i in range(20):
        ellipse(width/2 + randint(-5,5), rocket_position + randint(20,50), randint(5,10))

--- /code ---
</div>
   
--- task ---

**Test:** Run your program and you should see lots of grey circles in random places at the bottom of the rocket. 

--- /task ---

<div class="c-project-output">
![Circles with stoke - smoke effect.](images/rocket_lotscircles.png)
</div>
