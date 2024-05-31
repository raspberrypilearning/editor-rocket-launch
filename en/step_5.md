<h2 class="c-project-heading--task">Draw the rocket</h2>

--- task ---
Add a `rocket_y` global variable to keep track of the rocket's `y` position. 

Define a `draw_rocket()` function to make the rocket appear on the screen. 
--- /task --- 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 6 
line_highlights: 7
---

# Setup global variables    
screen_size = 400    
rocket_y = screen_size  

--- /code ---
</div>


<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11 
line_highlights: 12-13 
---

# The draw_rocket function goes here   
def draw_rocket():   
    global rocket_y       
    image(rocket, width/2, rocket_y, 64, 64)    


--- /code ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

The variable `rocket_y` is set to the `screen_size` at the start so that it begins right at the bottom edge of the screen. 

</div>






