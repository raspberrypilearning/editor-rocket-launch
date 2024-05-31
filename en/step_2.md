<h2 class="c-project-heading--task">Draw a planet</h2>

--- task ---
Add code to display an image of a planet using the `image()` function:

`image(image filename, x-coordinate, y-coordinate, image_width, image_height)
`

Use `image_mode(CENTER)` so that the x,y coordinate is the centre of the image not the top left corner. 
--- /task --- 

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18 
line_highlights: 22-23
---
def setup():  
    size(screen_size, screen_size)    
    global planet
    planet = load_image('planet.png') 
    image(planet, width/2, height, 300, 300)
    image_mode(CENTER)
--- /code ---
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Click on the image icon to the left to view the image gallery. 

If you want to use a different planet image, change `planet.png` in the code to a different filename, for example, `orange_planet.png`.

The line of code `from p5 import *` gives you global `width` and `height` variables based on the size of the screen. 

</div>

**Test:** Run your code and check that it draws a black background with half a planet at the bottom.

![A planet against a black background.](images/step_2.png){:width="300px"}









