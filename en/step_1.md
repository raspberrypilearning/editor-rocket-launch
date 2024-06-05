<h2 class="c-project-heading--task">Draw the background</h2>

--- task ---
➡️ Create a black background which will represent space.
--- /task --- 

Define a `draw_background()` function.
Set the background colour to black.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 12 
line_highlights: 13-14
---

# The draw_background function goes here   
def draw_background():   
    background(0, 0, 0)    
  
--- /code ---
</div>

Add this function to the list of things to `draw()` in every frame.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 23 
line_highlights: 25
---

def draw():
    # Things to do in every frame
    draw_background() 
  
--- /code ---
</div>

**Test:** Run your code and you should see a black square. 

<div class="c-project-callout c-project-callout--tip">

### Tip

The three numbers in `background(0, 0, 0)` are red, green and blue values. If you'd like your version of space to be a different colour, try changing these numbers to any whole number between 0 and 255.

</div>
