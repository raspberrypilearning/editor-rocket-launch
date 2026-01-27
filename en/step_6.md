<h2 class="c-project-heading--task">Draw the rocket</h2>

--- task ---
➡️ Make the rocket appear on the screen

--- /task --- 

Add a `rocket_position` global variable to keep track of the rocket's `y` position. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 6 
line_highlights: 8
---

# Setup global variables    
screen_size = 400    
rocket_position = screen_size  

--- /code ---
</div>


<div class="c-project-callout c-project-callout--tip">

### Tip

The `rocket_position` is set to the `screen_size` at the start so that the rocket appears right at the bottom edge of the screen. 

</div>

Define a `draw_rocket()` function to make the rocket appear on the screen.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 9 
line_highlights: 10-12 
---

# The draw_rocket function goes here   
def draw_rocket():   
    global rocket_position      
    image(rocket, width/2, rocket_position, 64, 64)    


--- /code ---
</div>

Call the `draw_rocket()` function.


<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 28 
line_highlights: 31 
---

def draw():
    # Things to do in every frame
    draw_background()
    draw_rocket() 


--- /code ---
</div>

**Test:** Run your code and check that the rocket appears at the bottom of the image. 





