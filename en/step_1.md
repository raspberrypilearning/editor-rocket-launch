<h2 class="c-project-heading--task">Draw the background</h2>

--- task ---
Create a black background which will represent space.

Define a `draw_background()` function and use `background(0, 0, 0)` to set the background colour to black.
--- /task --- 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 12 
line_highlights: 23-24
---

# The draw_background function goes here   
def draw_background():   
    background(0, 0, 0)    
  
--- /code ---
</div>

Call your new function inside the `draw()` function which has been made for you:

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 23 
line_highlights: 25
---

draw_background() 
  
--- /code ---
</div>