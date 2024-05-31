<h2 class="c-project-heading--task">Draw the background</h2>

--- task ---
Choose a planet to blast off from.

Click on the image icon to the left to view the image gallery. 

If you want to use a different planet image, change `planet.png` in the code to a different filename, for example, `orange_planet.png`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18 
line_highlights: 20
---
def setup():  
    size(screen_size, screen_size)    
    planet = load_image('planet.png') 
--- /code ---
--- /task ---



![A planet against a black background.](images/step_2.png){:width="300px"}
 The `image()` function is laid out:

`image(image filename, x-coordinate, y-coordinate, image_width, image_height)

`

The line of code `from p5 import *` gives you global `width` and `height` variables based on the size of the screen. Use these in your code to position the planet with its centre half-way across (`width/2`) and at the bottom (`height`) of the screen.

--- task ---

To make the background appear, call `draw_background()` in `draw()`. This will cause the background to be re-drawn every time `draw()` is called, covering over any older drawing:

--- code ---
---
language: python
filename: main.py — draw()
line_numbers: true
line_number_start: 28 
line_highlights: 30
---

def draw():   
    # Things to do in every frame    
    draw_background()
  
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and check that it draws a black background with half a planet at the bottom.

--- /task ---

If you have a Raspberry Pi account, on your code editor you can click on the **Save** button to save a copy of your project to your Projects.

--- save ---
