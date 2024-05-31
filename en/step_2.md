<h2 class="c-project-heading--task">Draw a planet</h2>

--- task ---
Add code to display an image of a planet using the `image()` function, which takes:

- image filename
- x coordinate
- y coordinate
- image width
- image height

Use `image_mode(CENTER)` so that the x,y coordinate you provide is the centre of the image not the top left corner. 
--- /task --- 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 12 
line_highlights: 14-15
---
def draw_background()):  
    background(0,0,0)
    image(planet, screen_size/2, screen_size, 300, 300)
    image_mode(CENTER)
--- /code ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

The x coordinate for the planet is `screen_size/2` to make the centre half way across the black square, horizontally. 

The y coordinate for the planet is `screen_size` to make the planet's centre right at the bottom of the black square.

</div>

**Test:** Run your code and check that it draws a black background with half a planet at the bottom.

![A planet against a black background.](images/step_2.png){:width="300px"}









