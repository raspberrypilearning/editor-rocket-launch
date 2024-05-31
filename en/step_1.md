<h2 class="c-project-heading--task">Draw the background</h2>

--- task ---
Create a black background which will represent space.

Define a `draw_background()` function and set the background colour to black.
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

Call this function inside the `draw()` function:

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


<div class="c-project-callout c-project-callout--tip">

### Tip

When you type an opening bracket `(`{:.language-python} the code editor will automatically add a closing bracket `)`{:.language-python} 
This also happens when you type an opening apostrophe `'`{:.language-python}.

</div>

<div class="c-project callout c-project-callout--tip">

### Tip

The three numbers in `background(0, 0, 0)` are red, green and blue values. If you'd like your version of space to be a different colour, try changing these numbers to any whole number between 0-255.

</div>
